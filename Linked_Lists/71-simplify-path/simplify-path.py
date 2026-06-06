class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        # 1. Split the path by '/' to get full directory names
        component = path.split('/')

        for part in component:
            if part == '..':
                if stack:
                    stack.pop()
            elif part == '.' or part == '':
                continue
            else:
                stack.append(part)


        res = "/" + "/".join(stack)
        return res       
