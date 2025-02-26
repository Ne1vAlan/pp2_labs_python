import re

pattern = r"ab{2,3}"

def match(a):
    if re.fullmatch(pattern, a):
        return "Found a match!"
    else:
        return "Not match!"
    
text = "Davai suda svoi string"
print(match(text))
    

    