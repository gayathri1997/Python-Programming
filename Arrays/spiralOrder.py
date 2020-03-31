def spiralOrder(matrix):
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m-1
        left, right = 0, n-1
        res = []
        while top<bottom and left < right:
            for i in range(left, right):
                res.append(matrix[top][i])
            for i in range(top, bottom):
                res.append(matrix[i][right])
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])
            top+=1
            bottom-=1
            left+=1
            right-=1
        
        if left == right:
            for i in range(top, bottom+1):
                res.append(matrix[i][left])
        elif top == bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])

        return res
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(spiralOrder(matrix))
