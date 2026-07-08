class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        vis = [False]*n
        count = 0
        def dfs(i):
            nonlocal vis
            vis[i] = True
            for j in range(m):
                if not vis[j] and isConnected[i][j] == 1:
                    dfs(j)
        for i in range(n):
            if not vis[i]:
                dfs(i)
                count += 1
        return count