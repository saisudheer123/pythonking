nom=int(input())
list=[int(x) for x in input().split()]
z=sorted(list)
if((nom%2)!=0):
	print(z[nom//2])
else:
	w=int(nom/2)
	o=z[w]
	r=z[w-1]
	s=(o+r)/2
	print(s)
