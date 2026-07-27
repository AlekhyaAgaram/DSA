class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for ch in s:
            if ch.isalnum():
                l.append(ch.lower())

        i = 0
        j = len(l)-1

        while i<j:
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1

        return True
