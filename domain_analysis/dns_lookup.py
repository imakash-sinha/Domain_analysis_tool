# dns_lookup.py
import dns.resolver

def dns_lookup(domain):
    dns_records = {}
    record_types = ['A', 'MX', 'NS', 'TXT']

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            dns_records[record_type] = [str(rdata) for rdata in answers]
        except dns.resolver.NoAnswer:
            dns_records[record_type] = []

    return dns_records
