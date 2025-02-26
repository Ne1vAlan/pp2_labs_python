import re

pattern = r"([a-z])([A-Z])"

def match(a):
    snake = re.sub(pattern, r'\1_\2', a).lower()
    print(snake)

text = "DavaiSudaSvoiString"
match(text)