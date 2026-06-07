class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        i = (2 * len(nums)) - 1

        while i >= 0:
            c = nums[i % len(nums)]
            while stack and stack[-1] <= c:
                stack.pop()

            if i < len(nums):
                if not stack:
                    res[i] = -1
                else:
                    res[i] = stack[-1]
            stack.append(c)
            i -= 1

        return res

            
