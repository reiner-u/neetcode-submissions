class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest, highest, profit = prices[0], prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < lowest:
                lowest = prices[i]
                highest = 0
            elif prices[i] > highest:
                highest = prices[i]
            if highest-lowest>profit:    
                profit = highest - lowest
        if profit <= 0: return 0
        else: return profit