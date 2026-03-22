class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        min_l = float("+inf")
        sum = 0
        for r in range(len(nums)):            
            sum += nums[r]
            while sum >= target:
                min_l = min(min_l,r-l+1)
                sum -= nums[l]
                l+=1
        if min_l == float("inf"):
            return 0
        return min_l

        