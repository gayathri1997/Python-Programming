def leftRotation(a,d,n):
    for i in range(d):
        leftRotateByOne(a,n)
        
def leftRotateByOne(a,n):
    temp = a[0]
    for i in range(n-1):
        a[i] = a[i+1]
    a[n-1] = temp

a = [1,2,3,4,5,6,7]
print(a)
leftRotation(a,2,len(a))
print(a)