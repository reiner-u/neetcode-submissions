class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
            if prices[i]-lowest>profit:    
                profit = prices[i] - lowest
        if profit <= 0: return 0
        else: return profit