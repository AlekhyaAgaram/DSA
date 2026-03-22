class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_avg = float("-inf")
        l = 0
        window_sum = 0

        for r in range(len(nums)):
            window_sum += nums[r]

            if r >= k -1:
                max_avg = max(max_avg,window_sum)
                window_sum -= nums[l]
                l += 1

            
        return float(max_avg) /k
        
