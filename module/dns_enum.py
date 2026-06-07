import dns.resolver

def dns_enum(domain):
    results = {}
    record_types = ["A", "MX", "NS", "TXT"]

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            results[record] = [str(r) for r in answers]
        except dns.resolver.NoAnswer:
            results[record] = []
        except dns.resolver.NXDOMAIN:
            print(f"[DNS] Domain does not exist: {domain}")
            return None
        except Exception as e:
            print(f"[DNS] Error fetching {record} records: {e}")
            results[record] = []

    return results