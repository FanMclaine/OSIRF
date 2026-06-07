import whois

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return {
            "registrar": w.registrar,
            "creation_date": w.creation_date,
            "expiration_date": w.expiration_date,
            "name_servers": w.name_servers,
            "org": w.org,
            "country": w.country,
        }
    except whois.parser.PywhoisError:
        print(f"[WHOIS] Domain not found or unregistered: {domain}")
        return None
    except Exception as e:
        print(f"[WHOIS] Unexpected error: {e}")
        return None