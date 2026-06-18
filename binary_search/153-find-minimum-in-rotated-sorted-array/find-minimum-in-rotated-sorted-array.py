class Solution:
    def findMin(self, nums: List[int]) -> int:

            l = 0
            r = len(nums) - 1
            res = nums[0]

            while l <= r:
                mid = (l+r)//2

                if nums[l] <= nums[r]:
                    res = min(res, nums[l])
                    break

                # If mid element is greater than the right element,the minimum is definitely in the right half.
                if nums[mid] > nums[r]:
                    l = mid + 1
                # Otherwise, the minimum is at mid or to the left.
                else:
                    r = mid 
            return res