import ssl
import socket
from urllib.parse import urlparse

def check_ssl_certificate(url):
    """
    Checks if a URL has a valid SSL certificate.
    Returns 1 if valid, 0 if invalid or not found.
    """
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc
        
        if not hostname:
            return 0
        
       
        hostname = hostname.split(':')[0]
        
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                if cert:
                    return 1
        return 0
    except Exception:
        return 0