import re

def extract_ip_addresses(text):
    return re.findall(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b', text)

text = "Ping the server at 192.168.0.1 and 10.0.0.255."
print(extract_ip_addresses(text))
