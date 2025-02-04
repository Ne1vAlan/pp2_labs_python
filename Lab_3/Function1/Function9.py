import math

def Volume_of_sphere(Radius):
    pi = math.pi
    Result = ((4/3) * pi * (Radius ** 3))
    return Result, pi

Radius = int(input("enter your radius:"))
Result, pi = Volume_of_sphere(Radius)
print("V =", Result)
print("hint! the number of π ≈", pi)