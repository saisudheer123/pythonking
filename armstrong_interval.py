num1,num2=map(int,input().split())
for i in range(num1,num2):
	o=len(str(i))
	s=0
	t=i
	while(t>0):
		d=t%10
		s+=d**o
		t//=10
	if(i==s):
		print(i,end=' ')
