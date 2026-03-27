class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        freq = {}
        for i in magazine:
             freq[i] = freq.get(i,0)+1

        mp = {}
        for i in ransomNote:
            mp[i] = mp.get(i,0)+1
            if i in freq:
                if mp[i] > freq[i]:
                    return False
            else:
                return False
        return True

        