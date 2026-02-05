# SHA256 Hash Cracker

Offline SHA256 hash cracker using wordlist-based dictionary attacks.

## 🎯 Purpose

Demonstrates:
- Why weak passwords are vulnerable to offline attacks
- Dictionary attack methodology
- Difference between online vs offline password attacks
- Why password hashing alone isn't enough (salting required)

## 🚀 Usage
```bash
python3 SHA256_crack.py <hash> -w <wordlist>
```

### Examples
```bash
# Basic usage with default wordlist (rockyou.txt)
python3 SHA256_crack.py 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8

# Custom wordlist
python3 SHA256_crack.py 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 -w custom.txt

# Help
python3 SHA256_crack.py -h
```

## ✨ Features

- ✅ Wordlist-based dictionary attack
- ✅ Progress indicators (every 5,000 attempts)
- ✅ Error handling for missing wordlists
- ✅ Keyboard interrupt support (Ctrl+C)
- ✅ Attempt counter


## 🔍 How It Works

1. Reads target SHA256 hash from command line
2. Opens wordlist file
3. For each password:
   - Computes SHA256 hash
   - Compares with target hash
   - Reports match if found
4. Reports total attempts

## ⚠️ Limitations

- **Only works on unsalted hashes** (most real-world hashes are salted)
- **Single-threaded** (slow on large wordlists like rockyou.txt)
- **No GPU acceleration** (hashcat is faster for serious cracking)
- **Memory intensive** on very large wordlists

## 🎓 Educational Value

This project teaches:
- Why password complexity alone doesn't guarantee security
- Importance of salting in password storage
- Offline attack speeds (millions of hashes/second possible)
- Why rate limiting is critical for online authentication

## 🔐 Real-World Defense

To protect against these attacks:
- ✅ Use salted hashes (bcrypt, argon2, scrypt)
- ✅ Enforce strong password policies
- ✅ Implement rate limiting on login endpoints
- ✅ Use multi-factor authentication (MFA)

## ⚖️ Legal Disclaimer

For **educational purposes and authorized testing only**.  
Unauthorized access to computer systems is illegal.

## 📚 References

- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Understanding Password Hashing](https://crackstation.net/hashing-security.htm)

---

**Author:** Luka Mgeladze  
**Date:** February 2026  
**Course:** TCM Security Python 101
```

---

