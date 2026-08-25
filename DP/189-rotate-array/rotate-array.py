class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #uses extra space
        '''
        n = len(nums)
        arr = [0] * n
        for i in range(n):
            arr[(i + k) % n] = nums[i]
        nums[:] = arr
        '''
        n = len(nums)
        k = k%n

        def reverse(nums,l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1

        reverse(nums,0,n-1)
        reverse(nums,0,k-1)
        reverse(nums,k,n-1)