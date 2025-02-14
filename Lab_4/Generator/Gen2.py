def Generator(numbers):
    for numb in range(numbers + 1):
        if numb % 2 == 0:
            yield numb


numbers = int(input())
result = Generator(numbers)

print(",".join(str(num) for num in Generator(numbers)))