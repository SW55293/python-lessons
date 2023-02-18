# Pattern          = Sliding Window
# Time Complexity  = 
# Space Complexity = 
"""
Input1 = prices: List[int]
return type = int
"""

class Solution(object):
    def maxProfit(self, prices):

        max_profit = 0
        buy = 0 
        sell = 1
        
        while sell < len(prices):
            potential_profit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                max_profit = max(max_profit, potential_profit)
            else:
                buy = sell
            sell = sell + 1 #this gave me an error when it was in the else block
        return max_profit