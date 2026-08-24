class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        """
        memo = {}
        def dfs(m,n,i):

            if i < 0:
                return 0

            if (m,n,i) in memo:
                return memo[(m,n,i)]

            no_1 = 0
            no_0 = 0
            for j in strs[i]:
                if j == '1':
                    no_1 += 1
                else:
                    no_0 += 1

            take = 0
            skip = 0

            if no_1 <= n and no_0 <= m:
                take = 1 + dfs(m-no_0, n-no_1, i-1)
            skip = dfs(m,n,i-1) 

            memo[(m,n,i)] =  max(take,skip)
            return memo[(m,n,i)]
        return dfs(m,n,len(strs)-1)

        """

        #BOTTOM UP APPROACH
        dp = [[0]*(n+1) for _ in range(m+1)] 

        for s in strs:
            zero = s.count('0')
            one = s.count('1')

            for i in range(m, zero-1, -1):
                for j in range(n, one-1 , -1):
                    dp[i][j] = max(dp[i][j], 1+ dp[i-zero][j-one])
        return dp[m][n]
                        