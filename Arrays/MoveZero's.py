a = [0,1,0,3,12]
n = len(a)

for i in range(0, n):
    if a[i] == 0:
        for j in range(i,n-1):
            a[j] = a[j+1]
        a[n-1] = 0
            
print(a)
