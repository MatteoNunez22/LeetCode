class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 1
        
        dp = [1] * n
        res = 1
        
        for i in range(n-2, -1, -1):
            maxLength = 0
            for j in range(i+1, n):
                minNum = float("inf")
                if nums[j] < minNum and nums[i] < nums[j]:
                    minNum = nums[j]
                    if dp[j] + 1 > maxLength:
                        maxLength = dp[j]
            dp[i] = maxLength + 1
            if dp[i] > res:
                res = dp[i]
        
        print(dp)
        return res