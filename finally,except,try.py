a=10
b=0
try:
    print("Resource open")
    print(a/b)
except Exception as e:
    print(e)
finally:
    print("Resource closed")