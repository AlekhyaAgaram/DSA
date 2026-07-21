class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {num:True for num in nums}
        res = 0

        for num in mp:
            if num-1 not in mp:
                curr_num = num
                curr = 1

                while (curr_num + 1)in mp:
                    curr_num += 1
                    curr += 1
                res = max(res,curr)

        return res