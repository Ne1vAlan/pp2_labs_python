import re

pattern= r"(?=[A-Z])"

def match(a):
    split= re.split(pattern, text)
    result = ' '.join(split)
    print(result)
    
text = "DavaiSudaSvoiString"
match(text)
    