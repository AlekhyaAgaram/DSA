class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = [0]*n
        res[0] = nums[0]

        if nums == []:
            return 0

        for i in range(1,n):
            res[i] = max(nums[i],res[i-1]+nums[i])
        return max(res)

        
