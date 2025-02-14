def Generator(numbers):

    for numb in numbers:
        yield numb ** 2


numbers = list(map(int, input().split()))
result = Generator(numbers)

while True:
    try:
        print(next(result))
    except StopIteration:
        break
    

