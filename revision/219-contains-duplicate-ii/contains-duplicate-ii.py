class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        res = False
        mp = {}
        
        for i in range(len(nums)):
            if nums[i] in mp and abs(i-mp[nums[i]]) <= k:
                res = True
                break
            mp[nums[i]] = i
        return res
                
