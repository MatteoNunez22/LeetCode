class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n == 1: return 0
        
        maxProfit = 0
        low = 0
        high = 1
        while high < n:
            if prices[high] > prices[low]:
                maxProfit = max(prices[high] - prices[low], maxProfit)
            elif prices[high] < prices[low]:
                low = high
            high += 1
        
        return maxProfit
            