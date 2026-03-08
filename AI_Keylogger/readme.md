# AI-Powered Keylogger (Educational)

Advanced keylogger with AI-based sensitive data detection and remote exfiltration.

## Features

- Real-time keystroke capture
- AI analysis (EaseMate.ai integration)
- Automatic normalization (removes key artifacts)
- Risk classification (Urgent/useless)
- Discord webhook exfiltration
- Headless browser automation

## Tech Stack

- Python 3.x
- pynput (keyboard monitoring)
- Selenium (browser automation)
- BeautifulSoup4 (HTML parsing)
- Requests (HTTP exfiltration)

## Usage
```bash
pip install pynput selenium beautifulsoup4 requests
python keylogger.py
```

**Configuration:**
- Set Discord webhook URL in `self.webhook_url`
- Adjust timer interval (default: 60 seconds)

## How It Works

1. Captures keystrokes using pynput
2. Every 60 seconds, sends keystrokes to AI for analysis
3. AI normalizes text and detects sensitive data
4. Classifies risk level
5. Sends report to Discord webhook

## Educational Purpose

This tool demonstrates:
- Post-exploitation data exfiltration
- AI integration in offensive tools
- Evasion techniques (headless browsers)
- Real-world attack chains

## Legal Disclaimer

**For educational purposes and authorized testing only.**

Unauthorized use of keyloggers is illegal under:
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act - UK
- Similar laws worldwide

Always obtain explicit written authorization.

## Future Enhancements

- Multi-platform support (Linux, macOS)
- Encrypted exfiltration
- Screenshot capture
- Clipboard monitoring
- C2 server integration

---

**Author:** Luka Mgeladze  
**Date:** March 2026  
**Purpose:** AI Red Teaming Research
