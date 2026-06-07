class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        i = 0
        for i in range(len(temperatures)):
            if not stack:
                stack.append(0)
            while stack and ( temperatures[i] > temperatures[stack[-1]]):
                p = stack.pop()
                d = i - p
                res[p] = d
            stack.append(i)
        return res
            



