# O(N) solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        #  The best profit is always the largest difference between a future price and a past lowest price
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
