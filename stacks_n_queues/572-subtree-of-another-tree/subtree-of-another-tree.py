# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # If the main tree is empty, subRoot cannot be a subtree
        if not root: 
            return False

        
        def isSame(p,q):
            if p==q==None:
                return True
            if not p or not q or p.val != q.val:
                return False

            return isSame(p.left,q.left) and isSame(p.right,q.right)


        # If the current trees match, we found it
        if isSame(root, subRoot):
            # Check the left and right children recursively
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        """
    
        q1 = deque([root])

        while q1:
            n = len(q1)
            for i in range(n):
                node = q1.popleft()

                if node.val == subRoot.val:
                    if isSame(node,subRoot):
                        return True
                    
                if node.left: q1.append(node.left) 
                if node.right: q1.append(node.right) 

        
        return False

        """