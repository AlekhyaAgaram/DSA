class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        j = 0
        i = 0

        if s == "":
            return True

        while i < len(t) and  j < len(s):
            if(t[i] == s[j]):
                j += 1
            i +=1
        if j == len(s):
            return True
        return False
        