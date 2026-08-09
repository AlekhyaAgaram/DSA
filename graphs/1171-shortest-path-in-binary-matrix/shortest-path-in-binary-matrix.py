class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[-1]*n for _ in range(n)]

        q = deque([(0,0)])

        # 8 directions (including diagonals)
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        dist[0][0] = 1

        while q:
            r,c = q.popleft()
            if r == n - 1 and c == n - 1:
                return dist[r][c]
            for i,j in directions:
                row = r+i
                col = c+j
                if 0 <= row < n and 0<= col <n and grid[row][col] == 0:
                    if dist[row][col] == -1:
                        dist[row][col] = dist[r][c] + 1
                        q.append((row,col))
        return -1


