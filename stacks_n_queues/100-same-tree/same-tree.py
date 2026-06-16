# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        queue1 = [p]
        queue2 = [q]

        while queue1:
            n = len(queue1)
            for i in range(n):
                node1 = queue1.pop(0)
                node2 = queue2.pop(0)
                if node1.val != node2.val:
                    return False

                if node1.left and node2.left:
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                elif node1.left is None and node2.left is None:
                    pass
                else:
                    return False

                if node1.right and node2.right:
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                elif node1.right is None and node2.right is None:
                    pass
                else:
                    return False


        return True

