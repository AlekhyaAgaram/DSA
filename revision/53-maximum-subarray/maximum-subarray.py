class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """        
        n = len(nums)
        res = [0]*n
        res[0] = nums[0]

        if nums == []:
            return 0

        for i in range(1,n):
            res[i] = max(nums[i],res[i-1]+nums[i])
        return max(res)
        """
        curr = 0
        maxi = nums[0]

        for i in range(len(nums)):
            curr += nums[i]
            if maxi < curr:
                maxi = curr

            if curr < 0:
                curr = 0

            
        return maxi

        
