from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        profit = 0

        for price in prices[1:]:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)
        
        return profit
    
    def maxProf(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price

            current_profit = price - min_price 

            if current_profit > max_profit:
                max_profit = current_profit

        return max_profit
    

prices = [7,1,5,3,6,4]

sol = Solution()
print(sol.maxProf(prices))