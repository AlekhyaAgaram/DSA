class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        far = 0
        for i in range(len(nums)):
            if i > far:
                return False
            far = max(i+nums[i],far)
            if far >= len(nums)-1:
                return True
        return False