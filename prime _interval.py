n1,n2=map(int,input().split())
for n2 in range(n1+1,n2):
	for j in range(2,n2):
		if(n2%j==0):
		    break
	else:
		print(n2,end=' ')
