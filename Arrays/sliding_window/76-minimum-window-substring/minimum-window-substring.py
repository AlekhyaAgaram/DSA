class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        if m < n:
            return ""

        freq = {}
        for i in t:
            freq[i] = freq.get(i,0)+1

        # 'required' is the number of UNIQUE characters in t
        required = len(freq)
        l = 0
        seen = {}
        count = 0 #will count how many unique char satisfied
        res = ""
        min_len = float("inf")

        for r in range(m):
            char_r = s[r]
            seen[char_r] = seen.get(char_r, 0) + 1

            if char_r in freq and seen[char_r] == freq[char_r]:
                count += 1
            
            # While the window is "valid" (contains all characters of t)
            while count == required:
                # 1. Update the result if this window is smaller than what we've seen
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    res = s[l : r + 1]

                # 2. Try to shrink the window from the left
                char_l = s[l]
                seen[char_l] -= 1
                
                # If removing s[l] makes the window invalid, decrement count
                if char_l in freq and seen[char_l] < freq[char_l]:
                    count -= 1
                
                l += 1
             
        return res
