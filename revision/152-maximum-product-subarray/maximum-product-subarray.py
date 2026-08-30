class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        maxi = nums[0]
        mini = nums[0]
        result = nums[0]

        if n == 1:
            return nums[0]
        else:
            for i in range(1,n):
                curr = nums[i]
                temp_max = max(curr,maxi*curr,mini*curr)
                mini = min(curr, maxi * curr, mini * curr)
                maxi = temp_max
                result = max(result, maxi)
        return result

            
