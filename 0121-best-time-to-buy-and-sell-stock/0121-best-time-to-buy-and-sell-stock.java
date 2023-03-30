class Solution {
    public int maxProfit(int[] prices) {
        
        int maxProfit = 0;
        
        for (int l = 0, r = 1; r < prices.length; r++) {
            if (prices[r] < prices[l]) {
                l = r;  
            } else {
                int profit = prices[r] - prices[l];
                maxProfit = Math.max(maxProfit, profit);
            }
        }
        
        return maxProfit;
    }
}