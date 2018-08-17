nom=[str(x) for x in input().split()]
for i in range(0,len(nom)):
	if(i>=0):
		k=''
	else:k=' '
	print(nom[i],end=k)
