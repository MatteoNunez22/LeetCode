int maxProfit(int* prices, int pricesSize){

    int l = 0;
    int r = 1;
    int maxProfit = 0;
    
    while (r < pricesSize) {
        if (prices[l] <= prices[r]) {
            int profit = prices[r] - prices[l];
            if (profit > maxProfit) maxProfit = profit;
        } else {
            l = r;
        }
        r++;
    }
    
    return maxProfit;
}