class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        vis = [[False]*n for _ in range(m)]

        def dfs(r,c):
            if not(r in range(m) and c in range(n)):
                return 0
            if vis[r][c]:
                return 0
            if grid[r][c] == 0:
                return 0

            vis[r][c] = True

            return (1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c))

        ans = 0
        cnt = 0

        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 1:
                    cnt = dfs(i,j)
                ans = max(ans,cnt)
        return ans
