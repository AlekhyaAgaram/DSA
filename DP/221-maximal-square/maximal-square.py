class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        # we create a matrix with a dummy 0 row and col - witht his we avooid mulitple ifelse edge cases
        dp = [[0] *n for _ in range(m)]
        maxi = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i==0 or j==0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    maxi = max(maxi,dp[i][j])
        return (maxi*maxi)
        