import re

pattern= r"\b[a-z]+[a-z]+\b"

def match(a):
    if re.fullmatch(pattern, a):
        print ("Found a match!")
        print (f"result: {re.findall(pattern, a)}")
    else:
        return "Not match!"
    
text = "Davai suda svoi string"
print(match(text))