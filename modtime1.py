import time as t
initial=t.time()
print("Initial",initial)
for i in range(10):
	print("Tarun")
print(t.time()-initial)
initial2=t.time()
print("Initial 2",initial2)
j=0
while j<10:
	print("Tarun")
	j+=1
print(t.time()-initial2)
	