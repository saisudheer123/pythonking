nom=int(raw_input())
f1=0
f2=1
f=1
if (nom>0):
	for i in range(0,nom):
		print f,
		f=f1+f2
		f1=f2
		f2=f
