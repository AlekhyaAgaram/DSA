class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        res = 0
        for i in s:
            if(i == '('):
                depth += 1        

            if(depth > res):
                res = depth

            if(i == ')'):
                depth -= 1
        return res
        
                
            

        
        