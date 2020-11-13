#list Comprehension

# lis=[]
# for j in range(100):
#     if j%2==0:
#         lis.append(j)
# print(lis)

lst=[i for i in range(100) if i%2==0]
print(lst)

#dictionary comprehension
dict1={i:f"item{i}" for i in range(1,101)}
print(dict1)

#Reversing of dictionary

dict2={value:key for key,value in dict1.items()}
print(dict2)
print(dict1)

#Set Comprehension
dresses={dress for dress in ["dress1","dress2","dress1","dress2"]}
print(dresses)

#Generators using comprehension,to use comprehension in generator , use the parenthesis
evens=(i for i in range(100) if i%2==0)
print(next(evens))
print(next(evens))
print(next(evens))
print(next(evens))
#using generators in for loop we should not use __next__
for i in range(100):
    print(i)
