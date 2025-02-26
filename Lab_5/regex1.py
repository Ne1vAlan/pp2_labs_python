import re

pattern = r"ab*"
    
def match(txt):
    if re.findall(pattern, txt):
        return "Found a match!"
    else:
        return "Not match!"

text = "Davai suda svoi string"
print(match(text))