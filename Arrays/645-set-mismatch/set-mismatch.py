class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        mp = {i+1: 0 for i in range(len(nums))}
        lol=0
        lmao=0

        for i in nums:
            mp[i] += 1
            
        for i in mp:
            if mp[i]>1:
                lol = i
            if mp[i] == 0:
                lmao = i
        return [lol,lmao]
    
               
        
        