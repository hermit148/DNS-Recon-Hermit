# 🌐 DNS-RECONE - Automated DNS Misconfiguration Scanner  
**By HeRM!T**

```
██╗  ██╗███████╗██████╗ ███╗   ███╗██╗████████╗
██║  ██║██╔════╝██╔══██╗████╗ ████║██║╚══██╔══╝
███████║█████╗  ██████╔╝██╔████╔██║██║   ██║   
██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║   
██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║   ██║   
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   
        [ DNS-RECONE - by HeRM!T ]
```

---

## 🚀 Features
- ✅ Zone Transfer vulnerability check
- ✅ Subdomain enumeration (via `subfinder`)
- ✅ SPF, DKIM, and DMARC misconfiguration checks
- ✅ Open Resolver check (DNS Amplification)
- ✅ DNSSEC support check
- ✅ Auto-generated report

---

## ⚙️ Installation

### 🔧 Requirements:
- Python 3
- dig (dnsutils)
- grep
- subfinder

Install everything using:

```bash
chmod +x requirement.sh
./requirement.sh
```

Or install manually:

Make sure `$GOPATH/bin` is in your `$PATH`.

---

## 📦 Setup

Clone the repository:

Run the script:

```bash
python3 dns-recone.py
```

---

## 💻 Usage

When prompted, enter the target domain:

```
Enter the target domain (e.g., example.com): example.com
```

Results will be saved to:

```
example.com-result.txt
```

## ⚠️ Disclaimer

> This tool is built for **educational** and **authorized penetration testing** use only.  
> Do **NOT** run this against domains you do not own or have explicit permission to scan.

---

## 👨‍💻 Author

**HeRM!T** – Cybersecurity Enthusiast  

Happy Reconnaissance! 🕵️‍♂️
