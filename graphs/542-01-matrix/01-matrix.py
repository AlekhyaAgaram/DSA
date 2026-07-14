class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        q = deque()

        vis = [[0]*n for _ in range(m)]
        dist = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j,0))
                    vis[i][j] = 1
                else:
                    vis[i][j] = 0

        direc = [[-1,0],[1,0],[0,1],[0,-1]]

        while q:
            r,c,steps = q.popleft()
            dist[r][c] = steps

            for dr,dc in direc:
                newr = r + dr
                newc = c + dc

                if 0 <= newr < m and 0 <= newc < n and vis[newr][newc] == 0:
                    vis[newr][newc] = 1
                    q.append((newr,newc,steps+1))

        return dist
            


            

