def permute(a,l,r):
    if l==r:
        str = ''.join(a)
        if str[::-1] == str:
            print(str)
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i] = a[i],a[l]

a = list('ABA')
n = len(a)

permute(a,0,n-1) 
