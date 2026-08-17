class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i in range(len(s)):
            lastIdx [s[i]] = i

        res = []
        size = 0
        end = 0
        for i in range(len(s)):
            size += 1
            end = max(end,lastIdx[s[i]])
            if i == end:
                res.append(size)
                size = 0
        return res
