class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        coins.sort(reverse = True)
        n = len(coins)
        res = [0]*n
        a = 0

        if amount == 0:
            return 0
        else:
            rem = amount
            for i in range(n):
                res[i] = rem//coins[i]
                rem = rem%coins[i]
                a += res[i]
        if a == 0 or rem != 0:
            return -1
        else:
            return a
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
        

