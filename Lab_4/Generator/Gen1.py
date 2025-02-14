def Generator(numbers):

    for numb in range(numbers + 1):
        yield numb ** 2


numbers = int(input())
result = Generator(numbers)

while True:
    try:
        print(next(result))
    except StopIteration:
        break