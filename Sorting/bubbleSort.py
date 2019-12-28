def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]


arr = [1,3,2,5,4]

bubbleSort(arr)

for i in range(len(arr)):
	print (arr[i])
