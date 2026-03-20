class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # If needle is empty, return 0 per problem convention
        if not needle:
            return 0
            
        # .find() returns the index of the first occurrence
        # It returns -1 if the substring is not found
        return haystack.find(needle)