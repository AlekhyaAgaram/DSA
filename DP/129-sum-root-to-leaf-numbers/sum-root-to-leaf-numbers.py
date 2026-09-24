# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def dfs(node,val):
            if not node:
                return 0
            val = val*10 +node.val
            
            # 2. If it's a leaf, return the completed number
            if not node.left and not node.right:
                return val

            # 3. Sum paths from left and right subtrees
            return dfs(node.left, val) + dfs(node.right, val)
        
        return dfs(root,0)