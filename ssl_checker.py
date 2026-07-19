import ssl
import socket
import ipaddress
from urllib.parse import urlparse

def is_safe_hostname(hostname):
 
    blocked_hosts = ['localhost', '127.0.0.1', '0.0.0.0']
    if hostname.lower() in blocked_hosts:
        return False
    
    try:
        
        ip = socket.gethostbyname(hostname)
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local:
            return False
    except Exception:
        return False
    
    return True

def check_ssl_certificate(url):
    
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.netloc.split(':')[0]
        
        if not hostname:
            return 0
        
        
        if not is_safe_hostname(hostname):
            return 0
        
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                if cert:
                    return 1
        return 0
    except Exception:
        return 0
