def filter_prime(numbers):
    Primelist = []

    for number in numbers:
        if number > 1:
            is_prime = True
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break
            if is_prime:
                Primelist.append(number)
    return Primelist

numbers = list(map(int, input().split()))
Primelist = filter_prime(numbers)

print("Youre Prime list:", Primelist)


