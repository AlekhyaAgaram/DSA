class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        l = 0
        r = 0
        
        def expand(l,r) :
            # Expand outward as long as it's a valid palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # Return the length of the palindrome found
            # (right - left - 1) accounts for the extra loop step before failing
            return r - l - 1

        for i in range(len(s)):
            # Case 1: Odd length palindrome, center is at s[i]
            len1 = expand(i, i)
            # Case 2: Even length palindrome, center is between s[i] and s[i+1]
            len2 = expand(i, i + 1)
            
            # Take the maximum length found at this center
            max_len = max(len1, len2)
            
            # Update the bounding indices of the longest palindrome
            if max_len > r - l:
                l = i - (max_len - 1) // 2
                r = i + max_len // 2
                
        return s[l : r + 1]