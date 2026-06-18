# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return 0
        q = deque([root])
        res = []

        while q:
            n = len(q)
            lvl_sum = 0
            for i in range(n):
                node = q.popleft()

                lvl_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            lvl_avg = lvl_sum/n
            res.append(lvl_avg)
        return res