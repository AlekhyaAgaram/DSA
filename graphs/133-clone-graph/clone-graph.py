"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        mp = {}

        def dfs(node):
            if not node:
                return

            if node in mp:
                return mp[node]

            temp = Node(node.val)
            mp[node] = temp
            for i in range(len(node.neighbors)):

                l = dfs(node.neighbors[i])
                temp.neighbors.append(l)
            return temp

        return dfs(node)



