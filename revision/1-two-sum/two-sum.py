class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        res = []

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in mp:
                res.append(mp[rem])
                res.append(i)
            else:
                mp[nums[i]] = i

        return res