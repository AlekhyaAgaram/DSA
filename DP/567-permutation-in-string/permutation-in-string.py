class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)

        if k > len(s2):
           return False
        
        freq1 = {}
        freq2 = {}
        
        for ch in s1:
            freq1[ch] = freq1.get(ch,0)+1

        for i in range(k):
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1

        l = 0
        r = k

        while r < len(s2):
            if freq1 == freq2:
                return True

            # Remove left character
            freq2[s2[l]] -= 1

            if freq2[s2[l]] == 0:
                del freq2[s2[l]]

            # Add new right character
            freq2[s2[r]] = freq2.get(s2[r], 0) + 1

            l += 1
            r += 1

        return freq1 == freq2