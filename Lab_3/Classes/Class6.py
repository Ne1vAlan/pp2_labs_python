def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    return list(filter(lambda x: is_prime(x), numbers))


numbers = list(map(int, input().split()))
print("Prime numbers:", filter_primes(numbers))