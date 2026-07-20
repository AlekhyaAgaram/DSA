class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]*n
        res = -1

        prefix[0] = nums[0]

        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]

        for i in range(n):
            if i > 0:
                left_sum = prefix[i - 1] 
            else:
                left_sum = 0
            right_sum = prefix[n - 1] - prefix[i]

            if left_sum == right_sum:
                return i

        return -1