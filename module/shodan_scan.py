import shodan
import socket

def shodan_scan(domain, api_key):
    try:
        # resolve domain to IP first
        ip = socket.gethostbyname(domain)
    except socket.gaierror as e:
        print(f"[SHODAN] Could not resolve domain to IP: {e}")
        return None

    try:
        api = shodan.Shodan(api_key)
        host = api.host(ip)

        return {
            "ip": ip,
            "org": host.get("org", "N/A"),
            "isp": host.get("isp", "N/A"),
            "country": host.get("country_name", "N/A"),
            "city": host.get("city", "N/A"),
            "open_ports": host.get("ports", []),
            "vulns": list(host.get("vulns", [])),
            "services": [
                {
                    "port": service["port"],
                    "transport": service.get("transport", "N/A"),
                    "banner": service.get("data", "")[:100],  # trim banner
                }
                for service in host.get("data", [])
            ],
        }

    except shodan.APIError as e:
        print(f"[SHODAN] API Error: {e}")
        return None
    except Exception as e:
        print(f"[SHODAN] Unexpected error: {e}")
        return None