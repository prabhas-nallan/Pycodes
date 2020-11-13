import time
from functools import lru_cache

#lru_cache makes the latest time.sleep function
@lru_cache(maxsize=32)
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n
if __name__=="__main__":
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Calling Again")
    a=input("Enter something ")
    some_work(3)
    print("Called Again")