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

                # If left half is sorted, the minimum must be in the right half
                if nums[mid] > nums[r]:
                    l = mid + 1
                # Otherwise, the right half is sorted, so minimum is in the left half
                else:
                    r = mid 
            return res