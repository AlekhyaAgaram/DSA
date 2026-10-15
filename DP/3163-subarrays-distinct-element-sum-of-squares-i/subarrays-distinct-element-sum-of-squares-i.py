class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                total += len(s) ** 2
                
        return total