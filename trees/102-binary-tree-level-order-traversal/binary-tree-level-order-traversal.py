# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        queue = deque([root])

        while queue:
            n = len(queue)
            curr_lvl = []

            for i in range(n):
                node = queue.popleft()
                curr_lvl.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                    
                if node.right is not None:
                    queue.append(node.right)
            res.append(curr_lvl)

        return res