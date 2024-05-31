# main.py
from domain_analysis.whois_lookup import whois_lookup
from domain_analysis.dns_lookup import dns_lookup
from domain_analysis.ssl_analysis import ssl_analysis

def main():
    domain = input("Enter a domain name: ")
    
    # Perform WHOIS lookup
    whois_info = whois_lookup(domain)
    print("WHOIS Information:")
    print(whois_info)
    
    # Perform DNS lookup
    dns_records = dns_lookup(domain)
    print("\nDNS Records:")
    for record_type, records in dns_records.items():
        print(f"{record_type}: {', '.join(records)}")
    
    # Perform SSL analysis
    ssl_info = ssl_analysis(domain)
    print("\nSSL Certificate Information:")
    print(ssl_info)

if __name__ == "__main__":
    main()
