num=int(input("Enter a number "))
if num==0 or num==1:
    print(f"The number {num} is not prime")
for i in range(2,num):
    if num%i==0:
        print(f"The number {num} is not prime")
        break
else:
    print(f'The number {num} is prime')