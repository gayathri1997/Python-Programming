'''
Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

temp=[]
n=len(matrix)
for i in range(n):
    temp1=[]
    for j in range(n-1,-1,-1):
        print(matrix[j][i])
        temp1.append(matrix[j][i])
    temp.append(temp1)
matrix.clear()
matrix.extend(temp)
