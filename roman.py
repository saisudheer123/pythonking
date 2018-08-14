nom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
b=[str(x)for x in input()]
s=0
for i in range(0,len(b)):
    if i>0 and nom[b[i]] > nom[b[i-1]]:
        s=nom[b[i]]-nom[b[i-1]]
    else:
        s+=nom[b[i]]
print(s)
