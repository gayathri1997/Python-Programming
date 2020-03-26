a = [1,2,4,5,6]
result = False

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            result = True
            break
            
print(result)
