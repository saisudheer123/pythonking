nom=int(raw_input())
list=[int(x) for x in raw_input().split()]
z=sorted(list)
for w in range(nom):
	print z[w],
