def KLargest(arr, k) :
    
    arr.sort( reverse = True)
    
    for i in range(k) :
        print(arr[i],end=" ");


k = 3
arr = [1,5,2,6,4]

KLargest(arr,k)
