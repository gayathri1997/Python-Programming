def selectionSort(arr): 
 
	for i in range(len(arr)): 
		min_index = i
		
		for j in range(i+1,len(arr)) :
			if arr[min_index] > arr[j] :
				min_index = j
		
		arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [1,3,4,2,5] 
selectionSort(arr) 

for i in range(len(arr)): 
	print (arr[i]) 
