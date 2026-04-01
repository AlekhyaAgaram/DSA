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

            """
            if mp[i] > 1:
                if i+1 not in nums and i+1 <= len(nums):
                    return[i,i+1]
                elif i-1 not in nums:
                    return [i,i-1]
            """
        for i in mp:
            if mp[i]>1:
                lol = i
            if mp[i] == 0:
                lmao = i
        return [lol,lmao]
    
               
        
        