l = [1,10,3,7,4]
print(l)

firstmax = max(l[0],l[1])
secondmax = min(l[0],l[1])

for i in range(2,len(l)):
    if l[i] > firstmax:
        secondmax = firstmax
        firstmax = l[i]
    else:
        if l[i] > secondmax:
            secondmax = l[i]
           
print('Second highest element : ' + str(secondmax))