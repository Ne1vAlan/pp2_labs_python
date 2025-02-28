def calc(s):
    uppers = sum(map(str.isupper, s))
    lowers = sum(map(str.islower, s))

    return(uppers, lowers)

a = "HelloHowAreYou"

print(calc(a))