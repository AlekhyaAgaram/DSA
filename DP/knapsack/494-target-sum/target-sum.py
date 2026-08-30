class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if abs(target) > total or (total + target) % 2 != 0:
            return 0

        s1 = (total + target) // 2
        n = len(nums)
        dp = [[0] * (s1 + 1) for _ in range(n + 1)]

        dp[0][0] = 1

        for i in range(1,n+1):
            curr = nums[i - 1]
            for t in range(s1+1):
                take = 0
                if t >= curr:
                    take = dp[i-1][t-curr]
                skip = dp[i-1][t]
                dp[i][t] = skip + take

        return dp[n][s1]



        """
        dp = {}  # (index, total) 

        def backtrack(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = (backtrack(i + 1, total + nums[i]) +
                              backtrack(i + 1, total - nums[i]))
            return dp[(i, total)]

        return backtrack(0, 0)
        """

