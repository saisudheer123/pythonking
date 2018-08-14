nom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
bom=[str(q)for q in input()]
s=0
for i in range(0,len(bom)):
    if i>0 and nom[bom[i]] > nom[bom[i-1]]:
        s=nom[bom[i]]-nom[bom[i-1]]
    else:
        s+=nom[bom[i]]
print(s)
