from functools import lru_cache
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        INF = float('-inf')

        @lru_cache(None)
        def dp(r1,c1,r2):
            #compute col of person B
            c2 = r1+c1-r2

            #check if any coord out of bounds
            if r1>=n or c1>=n or r2>=n or c2 >= n:
                return INF

            #check if any obsatcle in path of A or B
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return INF

            #if end reached return cell
            if r1==n-1 and c1==n-1:
                return grid[n-1][n-1]

            #if both A n B are on same cell- pick cherry only once
            if r1==r2 and c1==c2:
                cherries = grid[r1][c1]
            else:
                cherries = grid[r1][c1] + grid[r2][c2]

            #calculate all different ways A and B can move
            d_d = dp(r1+1 ,c1 , r2+1)
            d_r = dp(r1+1 ,c1 , r2)
            r_d = dp(r1 ,c1+1 , r2+1)
            r_r = dp(r1 ,c1+1 , r2)

            best = max(d_d ,d_r ,r_d ,r_r)
            return cherries + best

        res = dp(0,0,0)
        return max(0,res)