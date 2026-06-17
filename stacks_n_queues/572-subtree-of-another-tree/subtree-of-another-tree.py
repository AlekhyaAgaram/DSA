# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q1 = [root]

        def isSame(p,q):
            if p==q==None:
                return True
            elif p==None and q!=None: 
                return False
            elif p!=None and q==None:
                return False
            elif p.val != q.val:
                return False

            return isSame(p.left,q.left) and isSame(p.right,q.right)
    

        while q1:
            n = len(q1)
            for i in range(n):
                node = q1.pop(0)

                if node.val == subRoot.val:
                    if isSame(node,subRoot):
                        return True
                    
                if node.left: q1.append(node.left) 
                if node.right: q1.append(node.right) 

        
        return False