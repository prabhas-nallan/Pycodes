#import sys
import time as t
eppoch=print(t.time())
#print(sys.path)

import file2 as f2
print(f2.a)
lst=["Tarun",1,100,100]
sts=f2.show(*lst)
print(sts)

sum=f2.add(1,2,3,4)
print(f"The sum of numbers is {sum}")
print("Hello time")
print("Hello eppoch")