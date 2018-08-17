lst1=[int(x) for x in input().split()]
lst2=[int(y) for y in input().split()]
h=lst1[0]-lst2[0]
m=lst1[1]-lst2[1]
if(h<0 or m<0):
	print(-int(h),-int(m))
else:
	print(int(h),int(m))
