class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if number <2, alreavdy valid
        if len(nums) <= 2:
            return len(nums)

        i = 2 
        for j in range(2, len(nums)):
            # if current number is not equal to 2 numbers before  = keep it
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1

        return i