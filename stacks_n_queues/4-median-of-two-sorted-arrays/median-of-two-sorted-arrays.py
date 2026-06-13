class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)        
        n = len(res)
        if n%2 == 0:
            return (res[(n // 2) - 1] + res[n // 2]) / 2
        else:
            return res[n // 2]

