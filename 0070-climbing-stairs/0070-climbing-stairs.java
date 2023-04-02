class Solution {
    public int climbStairs(int n) {
        if (n < 2) return 1;
        
        int[] memo = new int[n+1];
        Arrays.fill(memo, 0);
        memo[0] = 1;
        memo[1] = 1;
        return recClimbStairs(n, memo);
    }
    
    public int recClimbStairs(int n, int[] memo) {
        if (memo[n] != 0) return memo[n];
        
        memo[n] = recClimbStairs(n-1, memo) + recClimbStairs(n-2, memo);
        return memo[n];
    }
}