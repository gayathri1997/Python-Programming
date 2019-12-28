def partition(a,low,high) :
	i = low - 1
	pivot = a[high]
	
	for j in range(low,high) :
		if a[j] <= pivot :
			i = i + 1
			a[i], a[j] = a[j], a[i]
	a[i+1], a[high] = a[high], a[i+1]
	return (i+1)

def quickSort(a,low,high) :
	
	if low < high :
		pi = partition(a,low,high)
		quickSort(a,low,pi-1)
		quickSort(a,pi+1,high)
		
a = [5,2,3,1,4]
n = len(a)
quickSort(a,0,n-1)
for i in range(n):
	print (a[i])