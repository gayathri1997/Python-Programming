class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if(not grid):
            return 0
        count,n,m = 0,len(grid), len(grid[0])
        
        def dfs(r,c):
            if(r<0 or r>n-1 or c<0 or c>m-1):
                return
            if(grid[r][c]=="1"):
                grid[r][c]="0"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
                
        for i in range(n):
            for j in range(m):
                if(grid[i][j]=="1"):
                    dfs(i,j)
                    count+=1
        return (count)
