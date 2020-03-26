# list of sorted numbers
a = [0,0,1,1,2,2,43,43,87,89]

j = 0
# n is length of the list
n = len(a)

# temp list to store the elements
temp = list(range(n))

for i in range(0,n-1):
    if a[i] != a[i+1]:
        temp[j] = a[i]
        j += 1

# store the last element as it is not stored previously
temp[j] = a[n-1]
j +=1

# print only the unique elements
for i in range(0,j):
    print(temp[i], end=" ")
    
    
