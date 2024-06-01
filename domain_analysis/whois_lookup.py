# whois_lookup.py
import whois

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except whois.parser.PywhoisError as e:
        return str(e)
