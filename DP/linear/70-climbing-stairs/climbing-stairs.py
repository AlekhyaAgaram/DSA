class Solution:
    def climbStairs(self, n: int) -> int:
        F = [0]*(n)
        if n <= 2:
            return n
        else:
            F[0] = 1
            F[1] = 2
            for i in range(2,n):
                F[i] = F[i-2]+F[i-1]
        return F[n-1]
                