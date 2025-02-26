import re

pattern = r"_(.)"

def match(a):
    camel = re.sub(pattern, lambda match: match.group(1).upper(), text)
    print(camel[0].lower()+camel[1:])
    
text = "Davai suda svoi string"
match(text)
    