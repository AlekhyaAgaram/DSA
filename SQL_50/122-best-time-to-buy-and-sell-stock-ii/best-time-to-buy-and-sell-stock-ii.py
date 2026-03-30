class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        
        # Start from the second day
        for i in range(1, len(prices)):
            # If the price today is higher than yesterday, take the profit
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        
        return max_profit
