class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific_set = set()
        atlantic_set = set()

        def dfs(r, c, visit_set):
            visit_set.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                row, col = r + dr, c + dc
                # Check boundaries, if already visited, and height condition 
                if (0 <= row < n and 0 <= col < m and 
                    (row, col) not in visit_set and 
                    heights[row][col] >= heights[r][c]):
                    dfs(row, col, visit_set)

        # 1. Run DFS for Pacific border (Top & Left)
        for i in range(n):
            dfs(i, 0, pacific_set)      # Left border
            dfs(i, m - 1, atlantic_set) # Right border

        # 2. Run DFS for Atlantic border (Bottom & Right)
        for j in range(m):
            dfs(0, j, pacific_set)      # Top border
            dfs(n - 1, j, atlantic_set) # Bottom border
        res = []
        for r,c in pacific_set:
            if (r,c) in atlantic_set:
                res.append([r,c])
        return res
        
                        
