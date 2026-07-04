class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        tot_sum = 0

        for i in range(n):
            tot_sum += nums[i]

        if tot_sum%2 == 1:
            return False

        target = tot_sum/2

        sums = {0}

        for num in nums:
            curr = list(sums)
            for i in curr:
                new = i + num
                if new == target:
                    return True
                elif new < target:
                    sums.add(new)

        return False