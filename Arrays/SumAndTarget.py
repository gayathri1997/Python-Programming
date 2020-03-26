'''

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

a = [2, 7, 11, 15]
target = 9

n = len(a)
for i in range(0,n-1):
    for j in range(i+1,n):
        if a[i] + a[j] == target:
            print(i,j) 
