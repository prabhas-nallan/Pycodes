lst=["Tarun","Taruni"]
#e=enumerate(lst)
print(list(enumerate(lst,2)))

s1="geeks"
print(list(enumerate(s1,1)))

for ele,i in enumerate(lst,1):
	print(i,ele)
for ele in enumerate(lst,1):
	print(ele)
