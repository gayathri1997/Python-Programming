def findDiagonalOrder(matrix):
        
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        for i in range(m+n-1):
            temp = []
            if i < m :
                row, col = 0,i
            else:
                row, col = i-n+1, n-1
                
            while row < m and col >= 0:
                temp.append(matrix[row][col])
                row += 1
                col -= 1
                
            if i%2:
                result.extend(temp)
            else:
                result.extend(temp[::-1])
                
                
        return result
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(findDiagonalOrder(matrix))
