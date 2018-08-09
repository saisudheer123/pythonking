nom=int(input())
x=[int(q) for q in input().split()]
z=sorted(x)
for w in range(nom):
	print(z[w],end=' ')
