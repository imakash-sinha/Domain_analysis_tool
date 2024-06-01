# ssl_analysis.py
import ssl
import OpenSSL

def ssl_analysis(domain):
    try:
        cert = ssl.get_server_certificate((domain, 443))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        subject = x509.get_subject()
        issuer = x509.get_issuer()
        expiration_date = x509.get_notAfter().decode("utf-8")
        
        ssl_info = {
            "Subject": dict(subject.get_components()),
            "Issuer": dict(issuer.get_components()),
            "Expiration Date": expiration_date
        }
        return ssl_info
    except Exception as e:
        return str(e)
