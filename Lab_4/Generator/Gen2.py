def Generator(number):
    for numb in range(number + 1):
        if numb % 2 == 0:
            yield numb


number = int(input())
result = Generator(number)

print(",".join(str(num) for num in Generator(number)))