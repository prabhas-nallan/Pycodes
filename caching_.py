from functools import lru_cache
import time
@lru_cache(maxsize=16)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
t1=time.time()
print([fib(n) for n in range(32)])
t2=time.time()
print(t2-t1)