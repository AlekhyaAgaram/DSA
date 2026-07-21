class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}

        curr = 0
        cnt = 0
        for i in range(len(nums)):
            curr += nums[i]
            needed = curr - k

            if needed in seen:
                cnt += seen[needed]

            seen[curr] = seen.get(curr, 0) + 1
        return cnt