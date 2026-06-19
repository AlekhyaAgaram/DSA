# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        prev = None
        minDiff =  float('inf')

        def dfs(node):
            nonlocal prev
            nonlocal minDiff
            
            if not node:
                return

            dfs(node.left)

            if prev:
                minDiff = min(minDiff, abs(node.val - prev.val))
            
            prev = node

            dfs(node.right)

        dfs(root) 
        return minDiff