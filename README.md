# Cybersecurity Projects

Python-based penetration testing tools built while learning offensive security and ethical hacking.

## 🎯 Purpose

These projects demonstrate:
- Network reconnaissance and enumeration
- Web application security testing
- Cryptographic attack techniques
- Professional Python development practices

All tools are for **educational purposes and authorized testing only**.

## 📂 Projects

### [1. TCP Port Scanner](./tcp-port-scanner/)
Fast, multi-threaded TCP port scanner with flexible port range selection.

**Key Features:**
- Concurrent scanning with thread pool
- Custom port ranges and specific port selection
- Open/closed/filtered port detection
- Professional CLI with argparse

**Tech:** Python sockets, ThreadPoolExecutor, argparse

---

### [2. Web Login Brute-Force Tool](./Web Login Brute-Force Tool/)
Automated web login brute-forcer with intelligent success detection.

**Key Features:**
- Automatic success/failure detection
- Rate limiting awareness
- Single username or username list support
- Custom success indicators

**Tech:** Python requests, threading, HTTP POST

---

### [3. SHA256 Hash Cracker](./sha256-cracker/)
Offline SHA256 hash cracker using wordlist-based dictionary attacks.

**Key Features:**
- Dictionary attack methodology
- Progress tracking
- Memory-efficient wordlist processing
- Demonstrates offline attack speeds

**Tech:** Python hashlib, file I/O

---

## 🛠️ Technologies

- **Language:** Python 3.x
- **Core Libraries:** 
  - `socket` (network operations)
  - `requests` (HTTP operations)
  - `threading` / `concurrent.futures` (concurrency)
  - `argparse` (CLI interfaces)
  - `hashlib` (cryptographic operations)

## 📚 Learning Path

These projects were built following a structured learning approach:

1. **Foundation:** Python fundamentals, OOP, threading
2. **Networking:** Sockets, TCP/IP, port scanning
3. **Web Security:** HTTP requests, authentication attacks
4. **Cryptography:** Hashing, dictionary attacks

## ⚖️ Legal Disclaimer

**For educational purposes and authorized testing only.**

Unauthorized access to computer systems is illegal under:
- Computer Fraud and Abuse Act (CFAA) - USA
- Computer Misuse Act - UK
- Similar laws worldwide

Always obtain explicit written authorization before testing any system you do not own.

## 🎓 Safe Testing Environments

Practice on:
- [HackTheBox](https://www.hackthebox.eu/)
- [TryHackMe](https://tryhackme.com/)
- [DVWA](http://www.dvwa.co.uk/)
- [bWAPP](http://www.itsecgames.com/)
- Your own lab environments

## 📧 Contact

**Luka Mgeladze**  
Cybersecurity Student | University of Caucasus  
Focus: Offensive Security, Penetration Testing

## 🚀 Future Projects

- Nmap automation and parser
- Directory brute-forcer
- Privilege escalation enumeration tool
- HTB machine writeups

---

*Built as part of a structured cybersecurity learning path combining TCM Security courses, personal projects, and HackTheBox practice.*
