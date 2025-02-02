def Palindrome(String):
    if String == String[::-1]:
        return True
    return False

String = input()
Result = Palindrome(String)
print(Result)