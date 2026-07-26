class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}

        for word in strs:
            s = "".join(sorted(word))
            if s in mp:
                mp[s].append(word)
            else:
                mp[s] = [word]
        return list(mp.values())

