# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if root is None:
            return []
        flag = True
        q = deque([root])
        res = []

        while q:
            n = len(q)
            curr = []
            for _ in range(n):
                node = q.popleft()
                curr.append(node.val)            
                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            if flag:
                res.append(curr)
            else:
                res.append(curr[::-1])
            flag = not flag
        return res
