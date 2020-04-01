def minSubArrayLen(s, nums):
        
    if sum(nums) < s:
        return 0
    if max(nums) >= s:
        return 1
    i, j, l = 0, 1, len(nums)
    min_length = l + 1
    while (i < l - 1) and (j < l):
        if sum(nums[i : j + 1]) < s:
            j += 1
        else:
            min_length = min(min_length, j - i + 1)
            i += 1
    return min_length
    
print(minSubArrayLen(7, [2,3,1,2,4,3]))
