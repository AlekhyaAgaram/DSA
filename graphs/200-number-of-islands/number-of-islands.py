class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[False]*n for _ in range(m)]        

        def dfs(r,c):
            if not(0 <= r <m and 0<= c <n):
                return
            if vis[r][c]:
                return
            if grid[r][c]=="0":
                return
            
            vis[r][c] = True
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not vis[i][j]:
                    dfs(i, j)
                    ans += 1
        return ans