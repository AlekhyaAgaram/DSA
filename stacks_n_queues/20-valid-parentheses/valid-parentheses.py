class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in mapping:
                # Check if stack is empty OR if the top doesn't match.
                if not stack or stack[-1]!= mapping[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        return False



