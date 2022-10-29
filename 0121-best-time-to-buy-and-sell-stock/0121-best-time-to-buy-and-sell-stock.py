class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n == 1: return 0
        
        maxProfit = 0
        low = 0
        high = 1
        for i in range(1, n):
            if prices[i] > prices[low]:
                high = i
                maxProfit = max(prices[high] - prices[low], maxProfit)
            elif prices[i] < prices[low]:
                low = i
                high = i
        
        return maxProfit
            