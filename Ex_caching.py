from functools import lru_cache
import time
num=int(input("Enter the value to be cached "))
@lru_cache(maxsize=num)
def add(a,b):
    print('Adding numbers')
    # time.sleep(3)
    # time.sleep(3)
    sum=a+b
    time.sleep(3)
    print(sum)
    time.sleep(3)
    print("Subtracting numbers")
    sub=a-b
    print(sub)

a=int(input("Enter a number "))
b=int(input("Enter another number "))
prove=add(a,b)