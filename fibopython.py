def fibbo(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        for i in range(n):
            print(i)
    else:
        for j in range(2,n):
            c=a+b
            a=b
            b=c
            if c<100:
                print(c)
        # else:
        #     print("Out of 100")

num=int(input("Enter a number "))
fibbo(num)