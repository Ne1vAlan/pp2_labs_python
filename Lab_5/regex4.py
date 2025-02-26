import re

pattern= r"\b[A-Z]+[a-z]+\b"

def match(a):
    if re.fullmatch(pattern, a):
        print ("Found a match!")
        print (f"result: {re.findall(pattern, a)}")
    else:
        print("Not match!")
    
text = "Davai suda svoi string"
print(match(text))
    

    