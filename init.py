sal = [1,2,4,5,67,657,32,834,9]
sal.sort()
k = 10

while sum(sal[:len(sal)-1]) > k :            
	del sal[-1]
else:
	print(len(sal))