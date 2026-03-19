class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        max_vol = (r-l)*min(height[l],height[r])

        while l<r:
            vol = (r-l)*min(height[l],height[r])
            max_vol = max(vol,max_vol)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_vol

        