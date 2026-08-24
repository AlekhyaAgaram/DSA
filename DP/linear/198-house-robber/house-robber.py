class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            dp[0] = nums[0]
            for i in range(1,n):
                dp[i] = max( dp[i-1],nums[i] + dp[i-2])
        return max(dp[n-1],dp[n-2])