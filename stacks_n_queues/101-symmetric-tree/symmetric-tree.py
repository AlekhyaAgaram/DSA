# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if p==q==None:
                return True
            elif not(p and q) or p.val!=q.val:
                return False
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        def invertTree(p):
            if p is None: return
            temp = p.left
            p.left = p.right
            p.right = temp
            if p.left:
                invertTree(p.left)
            if p.right:
                invertTree(p.right)
            return p

        q = invertTree(root.left)

        return isSame(q, root.right)