class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Step 1: Initialize the search space
        left = 1
        right = max(piles)
        res = right  # Store the best speed found so far

        # Step 2: Binary search
        while left <= right:
            mid = (left + right) // 2
            
            # Calculate total hours needed at speed 'mid'
            hours_spent = 0
            for pile in piles:
                hours_spent += math.ceil(pile / mid)
            
            # Step 3: Check if the speed is valid
            if hours_spent <= h:
                res = mid          # Valid speed, record it
                right = mid - 1    # Try to find a smaller valid speed
            else:
                left = mid + 1     # Too slow, increase the speed
                
        return res