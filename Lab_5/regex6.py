import re

pattern = r"[,.]"

def match(a):
    repl = re.sub(pattern, ";", text)
    print(repl)
    
text = "Davai, suda svoi string"
match(text)
    

    