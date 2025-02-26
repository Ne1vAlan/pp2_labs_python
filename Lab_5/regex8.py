import re

pattern = r"(?=[A-Z])"

def match(a):
    split = re.split(pattern, text)
    
    print(split)
    
text = "DavaiSudaSvoiString" 
match(text)
    