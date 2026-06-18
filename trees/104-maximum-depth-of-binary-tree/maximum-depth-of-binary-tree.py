# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        """
        #what i tried on my own

        depth = 0
        stack = [root]
        while stack:
            n = len(stack)
            for i in range(n):
                #supposed to use quqeue - instead pop from stack front
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if (node.right):
                    stack.append(node.right)
            depth += 1
        return depth

        """
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

    
