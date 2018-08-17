nom=int(input())
list=[int(x) for x in input().split()]
c=0
for i in range(0,nom):
	c=c+list[i]
print(int(c/nom))
