import re

def is_strong_password(password):
    if len(password) >= 8 and re.search(r'[\W_]', password):
        return True
    else:
        return False;

password = "Str0ng@Pwd"
print("Password is strong: ",is_strong_password(password))
