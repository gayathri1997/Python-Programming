'''

1. if the array is length is 0 then return "" else length is 1 then return the 1st element
2. if the size is more than 2 then 
      2.1 sort the array
      2.2 calculate the minimum length ( 1st and last element) => end
      2.3 loop from 0 to end and check 1st element and last element char by char if equal increse the i value
      2.4 return the a[0][0:i]

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        size = len(strs)
        
        if size == 0:
            return ""
        
        if size == 1:
            return strs[0]
        
        strs.sort()
        
        end = min(len(strs[0]), len(strs[size-1]))
        
        i = 0
        while i < end and strs[0][i] == strs[size-1][i]:
            i += 1
            
        return strs[0][0:i]
