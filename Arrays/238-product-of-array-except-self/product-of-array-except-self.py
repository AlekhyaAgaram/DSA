class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 1
        count = 0
        a =[]
        flag = False
        for i in nums:
            if i != 0:
                res = res*i
            elif i == 0:
                flag = True
                count += 1
            

        for i in nums:
            if count > 1:
                a.append(0)
            elif count == 1:
                if i == 0:
                    a.append(res)
                else:
                    a.append(0)
            else:
                a.append(res // i)
               
        return a
