# Pattern          = Sliding Window
# Time Complexity  = O(n)
# Space Complexity = O(1)
"""
Input1 = prices(List[int]) a list of integers
Return type = An (int) integer
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
            sell = sell + 1 #this gave me an error when it was in the else block. answer below
        return max_profit

# Answer to the error:
# I got an error because the sell counter wasnt updating
# it will only update when prices[buy] was greater than prices[sell]
# because thats when the else block would run. We need the sell
# counter to always update after ever go of the code no matter what.
# This will keep the code checking the next new sell price. 
#