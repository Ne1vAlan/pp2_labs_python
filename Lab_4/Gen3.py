def Generator(number):
    for numb in range(number + 1):
        if numb % 3 == 0 and numb % 4 == 0:
            yield numb

number = int(input())
result = Generator(number)

while True:
    try:
        print(next(result))
    except StopIteration:
        break