# TCP Port Scanner

Fast, multi-threaded TCP connect port scanner with flexible port range selection.

## 🚀 Usage
```bash
python scanner.py <target> [options]
```

### Examples
```bash
# Scan default ports (1-1000)
python scanner.py 192.168.1.1

# Custom port range
python scanner.py 192.168.1.1 -p 1-65535

# Specific ports
python scanner.py 192.168.1.1 -p 80,443,22,3389

# Verbose (show closed/filtered ports)
python scanner.py 192.168.1.1 -p 1-100 -v

# Custom thread count
python scanner.py 192.168.1.1 -p 1-1000 -t 200

# Help
python scanner.py -h
```

## ✨ Features

- ✅ **Multi-threaded scanning** - Thread pool for concurrent port checks
- ✅ **Flexible port selection** - Ranges (1-1000), lists (80,443), or single ports
- ✅ **Port state detection** - Open, closed, or filtered
- ✅ **Adjustable concurrency** - Control thread count for speed vs stealth
- ✅ **Verbose mode** - Optionally show all ports (not just open)
- ✅ **Hostname resolution** - Accepts IPs or hostnames

## 📋 Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `target` | ✅ Yes | Target IP or hostname |
| `-p, --ports` | ❌ No | Port range (default: 1-1000) |
| `-t, --threads` | ❌ No | Thread count (default: 100) |
| `-v, --verbose` | ❌ No | Show closed/filtered ports |

## 📋 Requirements
```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
# No external dependencies - uses Python standard library
```

## 🔍 How It Works

1. **Parse arguments** - Target, ports, threads, verbose mode
2. **Resolve hostname** - Convert domain to IP if needed
3. **Thread pool creation** - Create worker pool (default: 100 threads)
4. **Port scanning** - Each thread attempts TCP connection via three-way handshake
5. **State detection:**
   - `SYN → SYN/ACK` = **Open**
   - `SYN → RST` = **Closed**
   - `Timeout` = **Filtered** (firewall)
6. **Results display** - Show open ports (or all ports with `-v`)

## 🎓 Educational Value

This project teaches:
- TCP three-way handshake mechanics
- Socket programming in Python
- Thread pool management for I/O-bound tasks
- Port state classification (open/closed/filtered)
- Why filtered ports != closed ports (firewall behavior)

## ⚠️ Limitations

- **TCP connect scan only** (not stealth - leaves connection logs)
- **No SYN scan** (requires raw sockets / root privileges)
- **No service detection** (doesn't grab banners or identify services)
- **No UDP scanning** (TCP only)
- **Noisy** (target will log all connection attempts)

## 🔐 Real-World Defense

To protect against port scans:
- ✅ **Firewall rules** - Drop packets on unused ports (filtered state)
- ✅ **IDS/IPS** - Detect and block rapid connection attempts
- ✅ **Port knocking** - Hide services behind authentication sequences
- ✅ **Fail2ban** - Auto-ban IPs with suspicious patterns
- ✅ **Minimal attack surface** - Close unnecessary services

## 🆚 vs Nmap

| Feature | This Scanner | Nmap |
|---------|-------------|------|
| Speed | Fast (multi-threaded) | Very fast (optimized C) |
| Stealth | Noisy (connect scan) | Stealth options (SYN scan) |
| Service detection | No | Yes (-sV) |
| OS detection | No | Yes (-O) |
| UDP scanning | No | Yes (-sU) |
| Scripting | No | Yes (NSE) |

**Use this for:** Learning TCP mechanics, simple recon, custom automation  
**Use Nmap for:** Professional pentesting, comprehensive enumeration

## ⚖️ Legal Disclaimer

For **educational purposes and authorized testing only**.  
Unauthorized port scanning may be illegal in your jurisdiction.

## 📚 References

- [TCP Three-Way Handshake](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment)
- [Nmap Port Scanning Techniques](https://nmap.org/book/man-port-scanning-techniques.html)
- [Python Socket Programming](https://docs.python.org/3/library/socket.html)

---

**Author:** Luka Mgeladze  
**Date:** February 2026  
**Learning Path:** TCM Security Python 101 + Personal Projects
