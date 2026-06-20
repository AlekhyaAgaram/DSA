# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if node is None:
                return "null,"
            left = dfs(node.left)
            right = dfs(node.right)
            return str(node.val) + "," + left + right

        return dfs(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            val = vals[i]
            i += 1
            if val == "null":
                return None
            n = TreeNode(int(val))
            n.left = dfs()
            n.right = dfs()
            return n
        return dfs()

        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))