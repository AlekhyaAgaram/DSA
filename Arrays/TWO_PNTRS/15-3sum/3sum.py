class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        mp = {}

        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            req = - nums[i]
            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[l] + nums[r]
                if  total == req:
                    res.append([nums[i],nums[l],nums[r]])
                    # 1. Move both pointers inward FIRST
                    l += 1
                    r -= 1

                    # 2. THEN skip consecutive duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < req:
                    l += 1
                else:
                    r -= 1

        return res
