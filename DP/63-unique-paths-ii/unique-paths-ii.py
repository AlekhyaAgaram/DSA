class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            dp[0][j] = 1

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0

        return dp[m-1][n-1]
        """

        
        #THIS APPROACH GIVES STACK OVERFLOW FOR LARGE GRIDS
        def dfs(r,c):
            if r == m or c == n:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0

            if r == m-1 and c == n-1:
                return 1

            return dfs(r+1,c) + dfs(r,c+1)
        return dfs(0,0)
        """

