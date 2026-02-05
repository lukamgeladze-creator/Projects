import hashlib
import argparse
import time
from pathlib import Path

def crack_hash(target_hash, wordlists_path):
	if not Path(wordlists_path).exists():
		print(f"[!] Wordlist path not found: {wordlists_path}")
		return None
	attempts = 0
	print(f"[*] Cracking hash: {target_hash}")
	print(f"[*] Using Wordlist: {wordlists_path}")

	try:
		with open(wordlists_path, 'r', encoding = 'latin-1') as f:
			for line in f:
				password = line.strip()
				password_hash = hashlib.sha256(password.encode('latin-1')).hexdigest()

				if attempts % 5000 == 0:
					print(f'[*] Tried {attempts} passwrods...')
					time.sleep(1)

				if password_hash == target_hash:
					print(f'[+] Password found: {password}')
					print(f'[+] attempts taken: {attempts}')
					return password

				attempts += 1

		print(f'[-] Password not found after {attempts} tries')
		return None

	except KeyboardInterrupt:
		print(f'[-] The cracking has been interrupted')
		return None


def main():
    parser = argparse.ArgumentParser(description='SHA256 Hash Cracker')
    parser.add_argument('hash', help='Target SHA256 hash')
    parser.add_argument('-w', '--wordlist', default='rockyou.txt', 
                       help='Wordlist path (default: rockyou.txt)')
    args = parser.parse_args()
    
    crack_hash(args.hash, args.wordlist)

if __name__ == '__main__':
    main()
