a=input()
n1=0
w=0
new=[]
list=[int(x) for x in input().split()]
s=0
while(n1==0):
    l=list[n1]
    list.remove(list[0])
    if((l in list)and(l not in new)):
        print(l,end=" ")
        new.insert(w,l)
        w+=1
    elif((list==new) and (l not in new) and (s==len(new))):
        print('unique')
    if(list==[]):
        break
