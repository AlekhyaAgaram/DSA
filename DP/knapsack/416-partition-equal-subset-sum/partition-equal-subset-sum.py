import collections
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        tot_sum = 0

        for i in range(n):
            tot_sum += nums[i]

        if tot_sum%2 == 1:
            return False

        target = tot_sum//2
        
        dp = [False] * (target + 1)
        dp[0] = True

        for i in nums:
            for j in range(target, i-1, -1):
                dp[j] = dp[j] or dp[j-i]

        return dp[target]