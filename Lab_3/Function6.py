def Reverse_Words_strings(String):
    Result_String = list(reversed(String.split()))
    return Result_String

String = input()
Result_String = Reverse_Words_strings(String)
print("Your revers words:", " ".join(Result_String))