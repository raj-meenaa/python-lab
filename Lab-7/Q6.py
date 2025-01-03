import re

def extract_mobile_numbers(text):
    return re.findall(r'\b\d{10}\b', text)

text = "Contact us at 9876543210 or 1234567890 for support."
print(extract_mobile_numbers(text))
