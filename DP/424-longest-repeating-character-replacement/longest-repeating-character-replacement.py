class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        freq = {}
        max_freq = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq,freq[s[r]])
            while (r-l+1)-max_freq > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
            
        