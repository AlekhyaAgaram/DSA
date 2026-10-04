class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        dp = [float("inf")]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        if dp[amount] != float("inf"):
            return dp[amount]
        else:
            return -1
        """
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]

        for i in range(n+1):
            dp[i][0] = 0

        for i in range(1,n+1):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j] #dont take coin

                if coins[i-1] <= j:
                    dp[i][j] = min( dp[i][j], 1 + dp[i][j-coins[i-1]]) #take the coin

        return dp[n][amount] if dp[n][amount] != float('inf') else -1
        

