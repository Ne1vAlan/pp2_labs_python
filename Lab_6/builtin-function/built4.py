import time
import math

num = int(input())
delay = int(input())

time.sleep(delay / 1000)  

result = math.sqrt(num)

print(f"Square root of {num} after {delay} miliseconds is {result}")
