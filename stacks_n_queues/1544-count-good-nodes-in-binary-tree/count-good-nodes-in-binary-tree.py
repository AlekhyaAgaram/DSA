# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node,max_so_far):
            if node is None:
                return 0

            if node.val >= max_so_far:
                good = 1
            else:
                good = 0

            new_max = max(max_so_far,node.val)

            left = dfs(node.left,new_max)
            right = dfs(node.right,new_max)

            return good+left+right

        
        return dfs(root,root.val)


