class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1: return 1
        
        dp = [1] * n
        
        for i in range(n-2, -1, -1):
            maxLength = 1
            for j in range(i+1, n):
                if nums[i] < nums[j] and dp[j] + 1 > maxLength:
                    maxLength = dp[j] + 1 
            dp[i] = maxLength
        
        return max(dp)