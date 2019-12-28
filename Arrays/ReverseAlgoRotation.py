'''
    divide it into two parts 
    reverse each part 
    and finally reverse all the elements
'''

def reverseArray(a,start,end):
    while(start < end):
        a[start], a[end] = a[end],a[start]
        start += 1
        end -= 1
        
def arrayRotate(a,d):
    if d == 0:
        return 
    
    n = len(a)
    reverseArray(a,0,d-1)
    reverseArray(a,d,n-1)
    reverseArray(a,0,n-1)
    
arr = [1,2,3,4,5,6,7]
d = 2
arrayRotate(arr,d)
print(arr)