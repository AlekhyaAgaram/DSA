class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_vol = (r-l)*min(height[l],height[r])

        while l<r:
            vol = (r-l)*min(height[l],height[r])
            if vol > max_vol:
                max_vol = vol
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_vol
