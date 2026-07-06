class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1,n+1):
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:start + len(w)] == w:
                    dp[i] = True
                    break
        return dp[n]