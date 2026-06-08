# 🔍 Automated Reconnaissance & OSINT Framework for Passive Footprinting

<img width="480" height="437" alt="image" src="https://github.com/user-attachments/assets/372d3e90-a1df-4f46-9ca8-bb0d7f834227" />



A Python-based command-line tool that automates passive reconnaissance on a target domain — aggregating WHOIS data, DNS records, HTTP security header analysis, and Shodan intelligence into a structured terminal report.

Built as a portfolio project to demonstrate practical offensive security tooling and OSINT methodology.

---

## ✨ Features

- **WHOIS Lookup** — Registrar, creation/expiry dates, org, name servers
- **DNS Enumeration** — A, MX, NS, and TXT record extraction
- **HTTP Header Analysis** — Detects missing security headers (CSP, HSTS, X-Frame-Options, and more)
- **Shodan Intelligence** — Open ports, ISP, geolocation, detected services, and CVEs (if available)
- **Rich Terminal UI** — Colored tables, live spinners, and structured output via `rich`
- **Clean Report Output** — All findings printed per module with clear pass/fail indicators

---

## 🛠 Tech Stack

| Library | Purpose |
|---|---|
| `python-whois` | WHOIS domain registration data |
| `dnspython` | DNS record enumeration |
| `requests` | HTTP header fetching |
| `shodan` | Exposed service & vulnerability intel |
| `rich` | Terminal UI — tables, spinners, color |
| `python-dotenv` | Secure API key management |

---

## ⚡ Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/osint-framework.git
cd osint-framework
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Copy the example env file:
```bash
cp .env.example .env
```

Then edit `.env` and add your [Shodan API key](https://account.shodan.io/):
```
SHODAN_API_KEY=your_shodan_api_key_here
```

### 5. Run it
```bash
python main.py google.com
```

---

## 📁 Project Structure

```
osint-framework/
├── main.py                  # Entry point — CLI, spinners, report rendering
├── modules/
│   ├── whois_lookup.py      # WHOIS data extraction
│   ├── dns_enum.py          # DNS record enumeration
│   ├── header_check.py      # HTTP security header analysis
│   └── shodan_scan.py       # Shodan API intelligence
├── reports/                 # Output directory for saved reports
├── .env                     # Your secrets (gitignored)
├── .env.example             # Template for required env vars
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔐 Security Headers Checked

The header module flags the presence or absence of the following:

| Header | Purpose |
|---|---|
| `Strict-Transport-Security` | Enforces HTTPS |
| `Content-Security-Policy` | Prevents XSS |
| `X-Frame-Options` | Prevents clickjacking |
| `X-Content-Type-Options` | Prevents MIME sniffing |
| `Referrer-Policy` | Controls referrer info leakage |
| `Permissions-Policy` | Restricts browser feature access |

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes and authorized testing only**. Only run reconnaissance against domains you own or have explicit permission to test. Unauthorized scanning may violate laws in your jurisdiction.

---

## 🗺 Roadmap (v2)

- [ ] Export reports to `.txt` and `.json`
- [ ] Subdomain enumeration via wordlist bruteforce
- [ ] Email harvesting (Hunter.io API)
- [ ] Geolocation IP mapping with `folium`
- [ ] SSH Honeypot integration module
- [ ] Rate limiting & retry logic for API calls
