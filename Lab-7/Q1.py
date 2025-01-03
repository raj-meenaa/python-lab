import re

def find_emails(text):
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

text = "Contact us at info@example.com and support@domain.org."
print(find_emails(text))
