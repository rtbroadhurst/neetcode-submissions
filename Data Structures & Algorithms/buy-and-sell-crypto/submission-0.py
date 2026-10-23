class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Naive solution O(n^2)
        max_profit = 0
        for index, buy in enumerate(prices):
            for sell in prices[index + 1:]:
                profit = sell - buy
                if profit > max_profit:
                    max_profit = profit
        return max_profit
