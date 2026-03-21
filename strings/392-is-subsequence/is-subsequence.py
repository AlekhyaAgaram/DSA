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

        for char in t:
            if j<len(s) and char == s[j]:
                j+=1

        return j == len(s)
        