def Generator(number):
    while number >= 0:
        yield number
        number -= 1

n = int(input())

for number in Generator(n):
    print(number)