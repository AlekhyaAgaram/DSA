class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        l = 0
        r = len(numbers) - 1
        flag = False

        while(flag == False):
            if((numbers[l]+numbers[r]) == target):
                res.append(l+1)
                res.append(r+1)
                flag = True
            elif(numbers[l]+numbers[r] < target):
                l = l + 1
            elif(numbers[l]+numbers[r] > target):            
                r = r - 1
        return res