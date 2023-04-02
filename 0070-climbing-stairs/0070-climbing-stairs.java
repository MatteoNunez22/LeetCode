class Solution {
    // Top-down w/ memoization
    // public int climbStairs(int n) {
    //     if (n < 2) return 1;
    //     int[] memo = new int[n+1];
    //     Arrays.fill(memo, 0);
    //     memo[0] = 1;
    //     memo[1] = 1;
    //     return recClimbStairs(n, memo);
    // }
    // public int recClimbStairs(int n, int[] memo) {
    //     if (memo[n] != 0) return memo[n];
    //     memo[n] = recClimbStairs(n-1, memo) + recClimbStairs(n-2, memo);
    //     return memo[n];
    // }
    
    // Bottom-up
//     public int climbStairs(int n) {
//         if (n < 2) return 1;
//         int[] dp = new int[n+1];
//         dp[0] = 1;
//         dp[1] = 1;
        
//         for (int i = 2; i <= n; i++) {
//             dp[i] = dp[i-1] + dp[i-2];
//         }
//         return dp[n];
//     }
    
    // Optimal bottom-up
    public int climbStairs(int n) {
        if (n < 2) return 1;        
        int a = 1, b = 1, c;
        for (int i = 2; i <= n; i++) {
            c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
}