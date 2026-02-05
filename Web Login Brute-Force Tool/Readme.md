# Web Login Brute-Force Tool

Automated web login brute-force tool with intelligent success detection and flexible username/password list support.

## 🎯 Purpose

Demonstrates:
- HTTP POST-based authentication attacks
- Session handling and cookies
- Success/failure detection heuristics
- Rate limiting awareness
- Difference between online vs offline attacks

## 🚀 Usage
```bash
python3 login_brute.py <url> -u <username> -p <password_list> [options]
```

### Examples

**Single username:**
```bash
python3 login_brute.py http://target.com/login -u admin -p top-100.txt
```

**Multiple usernames:**
```bash
python3 login_brute.py http://target.com/login -U usernames.txt -p rockyou.txt
```

**Custom success indicator:**
```bash
python3 login_brute.py http://target.com/login -u admin -p passwords.txt -s "Welcome back"
```

**Help:**
```bash
python3 login_brute.py -h
```

## 📋 Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `url` | ✅ Yes | Target login URL (e.g., `http://site.com/login`) |
| `-u, --username` | ⚠️ * | Single username to test |
| `-U, --usernames` | ⚠️ * | Path to username wordlist |
| `-p, --passwords` | ✅ Yes | Path to password wordlist |
| `-s, --success` | ❌ No | Custom success indicator string |

*Either `-u` or `-U` must be provided

## ✨ Features

- ✅ **Automatic success detection** - No need to specify "needle" strings
- ✅ **Flexible input** - Single username or username list
- ✅ **Smart heuristics** - Detects login success via status codes and response content
- ✅ **Error handling** - Graceful timeout and connection error handling
- ✅ **Progress tracking** - Real-time attempt counter
- ✅ **Keyboard interrupt** - Clean exit with Ctrl+C

## 🔍 How Success Detection Works

### Automatic Mode (default):
The tool checks for successful login by:
1. **HTTP status code** - 200 (OK) or 302 (Redirect)
2. **Absence of error keywords** in response:
   - "invalid"
   - "incorrect"
   - "failed"
   - "wrong"
   - "error"

### Manual Mode (with `-s` flag):
Searches for your specified success string in the response.

**Example:**
```bash
-s "Dashboard"  # Looks for "Dashboard" in HTML response
-s "Welcome"    # Looks for "Welcome" text
```

## 📋 Requirements
```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
requests>=2.31.0
```

## 📁 Wordlist Examples

**usernames.txt:**
```
admin
administrator
root
user
test
```

**passwords.txt:**
```
password
123456
admin
letmein
welcome
```

## ⚠️ Limitations

- **Online attacks are slow** - Network latency limits speed
- **Rate limiting** - Many sites block after X failed attempts
- **CSRF tokens** - Modern sites may require token extraction
- **CAPTCHAs** - Cannot bypass automated detection
- **WAFs** - Web Application Firewalls may block requests
- **Account lockouts** - Risk of locking target accounts

## 🎓 Educational Value

This project teaches:
- HTTP POST request structure
- Form data submission
- Session and cookie handling
- Success/failure pattern recognition
- Why rate limiting is critical for web authentication
- Difference between online (slow) vs offline (fast) attacks

## 🔐 Real-World Defense

To protect against brute-force attacks:
- ✅ **Rate limiting** - Limit login attempts per IP/account
- ✅ **Account lockouts** - Temporary lockout after X failed attempts
- ✅ **CAPTCHA** - Require human verification after failures
- ✅ **Multi-factor authentication (MFA)** - Passwords alone aren't enough
- ✅ **Strong password policies** - Enforce minimum complexity
- ✅ **Login attempt monitoring** - Alert on suspicious patterns
- ✅ **IP blocking** - Block known malicious IPs

## 🛠️ Troubleshooting

### "No password found" but credentials are valid:
- Site may use different form field names (not `username`/`password`)
- May require additional fields (CSRF token, session ID)
- Use `-s` flag to specify custom success string

### Connection timeouts:
- Target site may be blocking your IP
- Increase timeout in code (default: 5 seconds)
- Add delays between requests

### False positives:
- Adjust success detection logic
- Use `-s` flag for specific success string
- Check HTTP response codes manually

## 🔧 Advanced Customization

### Custom form fields:
Edit line 24 to match target form:
```python
data={'username': username, 'password': password}
# Change to:
data={'user': username, 'pass': password}
```

### Add delays (rate limiting):
```python
import time
# Add after line 34:
time.sleep(1)  # 1 second delay between attempts
```

### Session persistence:
```python
# Add before brute_force_login():
session = requests.Session()
# Replace requests.post with:
r = session.post(...)
```

## ⚖️ Legal Disclaimer

**For educational purposes and authorized testing only.**

- ✅ Use on your own systems
- ✅ Use on intentionally vulnerable applications (DVWA, HackTheBox, etc.)
- ✅ Use with explicit written authorization

Unauthorized access to computer systems is **illegal** under:
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act - UK
- Similar laws worldwide

**Penalty:** Fines and/or imprisonment.

Always obtain proper authorization before testing.

## 📚 Testing Environments

Practice safely on:
- [DVWA (Damn Vulnerable Web Application)](http://www.dvwa.co.uk/)
- [bWAPP](http://www.itsecgames.com/)
- [HackTheBox](https://www.hackthebox.eu/)
- [TryHackMe](https://tryhackme.com/)
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/)

## 📖 References

- [OWASP Brute Force Attacks](https://owasp.org/www-community/attacks/Brute_force_attack)
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [CWE-307: Improper Restriction of Excessive Authentication Attempts](https://cwe.mitre.org/data/definitions/307.html)

## 🤝 Contributing

Improvements welcome:
- Better success detection heuristics
- CSRF token extraction
- Session handling improvements
- Multi-threading support

---

**Author:** Luka Mgeladze  
**Date:** February 2026  
**Course:** TCM Security Python 101  
**Purpose:** Educational demonstration of web authentication vulnerabilities
```

---

## Folder Structure
```
projects/
├── README.md
├── sha256-cracker/
│   ├── README.md
│   ├── SHA256_crack.py
│   └── requirements.txt
└── web-login-bruteforce/
    ├── README.md
    ├── login_brute.py
    └── requirements.txt
```

---

## requirements.txt for this project
```
requests>=2.31.0
