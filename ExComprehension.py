user_range=int(input("Enter the range you want for comprehensions "))

while(1):
    print("1 for List Comprehension")
    print("2 for dict Comprehension")
    print("3 for set Comprehension")
    print("4 for Quit")
    choice=int(input("Enter youe choice "))
    if choice==1:
        print("List Comprehension")
        lst=[i for i in range(user_range) if i%2==0]
        print(type(lst))
        print(lst)
    
    elif choice==2:
        print("Dict Comprehension")
        dict1={i:f"item{i}" for i in range(user_range) if i%2==0}
        print(type(dict1))
        print(dict1)
    
    elif choice==3:
        print("Set Comprehension")
        set1={i for i in range(user_range)}
        print(type(set1))
        print(set1)
    else:
        exit()


    
    
