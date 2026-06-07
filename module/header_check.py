import requests

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

def check_headers(domain):
    try:
        response = requests.get(f'https://{domain}', timeout=5)
    except requests.exceptions.SSLError:
        try:
            response = requests.get(f'http://{domain}', timeout=5)
        except requests.exceptions.RequestException as e:
            print(f"[HEADERS] Error: {e}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[HEADERS] Error: {e}")
        return None

    headers = dict(response.headers)
    missing = [h for h in SECURITY_HEADERS if h not in headers]
    present = {h: headers[h] for h in SECURITY_HEADERS if h in headers}

    return {
        "status_code": response.status_code,
        "server": headers.get("Server", "Not disclosed"),
        "x_powered_by": headers.get("X-Powered-By", "Not disclosed"),
        "security_headers_present": present,
        "security_headers_missing": missing,
    }