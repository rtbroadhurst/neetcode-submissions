class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = float('inf')
        largest_profit = 0
        for price in prices:
            profit = price - lowest_buy
            if profit > largest_profit:
                largest_profit = profit
            elif price < lowest_buy:
                lowest_buy = price
        return largest_profit
