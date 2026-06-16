# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
            
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1 :
                self.ans = False

            return 1 + max(left,right)
        
        
        dfs(root)
        return self.ans

        """

        if root is None:
            return True
        queue = [root]

        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                
                left = dfs(node.left)
                right = dfs(node.right)
                if abs(left - right) > 1:
                    return False

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
        return True
        """