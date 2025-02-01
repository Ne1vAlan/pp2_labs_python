import itertools

def String_For_User(String):
    String_Result = list(itertools.permutations(String))
    return String_Result

String = input()
String_Result = String_For_User(String)

print("Youre Words:", ["".join(split) for split in String_Result])