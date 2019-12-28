def permute(a,l,r,list):
    if l==r:
        if ''.join(a) not in list:
            list.append(''.join(a))
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r,list)
            a[l],a[i] = a[i],a[l]

a = list('ABA')
n = len(a)
list = []

permute(a,0,n-1,list) 

for i in list:
    print(i)