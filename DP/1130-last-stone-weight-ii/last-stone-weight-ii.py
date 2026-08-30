class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = 0
        for i in range(n):
            total += stones[i]

        dp = [[False]*(total+1) for _ in range(n+1)]

        dp[0][0] = True

        for i in range(1,n+1):
            for j in range(total+1):
                take = False
                if stones[i-1] <= j:
                    take = dp[i-1][j-stones[i-1]]
                skip = dp[i-1][j]
                dp[i][j] = take or skip
        ans = total
        for s in range(total//2 + 1):
            if dp[n][s]:
                ans = min(ans, total - 2*(s))

        return ans