def square(a, b):
    for numb in range(a,b + 1):
        yield numb ** 2

a = int(input())
b = int(input())

for n in square(a, b):
    print(n)