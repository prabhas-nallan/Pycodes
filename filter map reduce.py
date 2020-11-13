from functools import reduce
lis=[2,5,710,100,5,6,13,89]
evens=list(filter(lambda n:n%2==0,lis))
doubles=list(map(lambda num:num*2,evens))
print(evens)
print(doubles)
sum=reduce(lambda i,j:i+j,doubles)
print(sum)