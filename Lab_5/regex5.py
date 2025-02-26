import re

pattern= r"\b[a-z]+[b]$\b"

def match(a):
    if re.fullmatch(pattern, a):
        print ("Found a match!")
        print (f"result: {re.findall(pattern, a)}")
    else:
        print("Not match!")
    
text = "grab"
match(text)
    

    