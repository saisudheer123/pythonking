nom=input()
z=0
for i in range(0,len(nom)):
	c=int(nom)%10
	z=z+c
	nom=int(nom)//10
print(z)
