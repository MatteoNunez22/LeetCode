class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * n
        
        for i in range(n - 2, -1, -1):
            if nums[i] == 0:
                dp[i] = -1
                continue
                
            minJump = float("inf")
            for j in range(i + 1, min(i + 1 + nums[i], n)):
                if dp[j] != -1:
                    minJump = min(minJump, dp[j])
            dp[i] = minJump + 1
            
        return dp[0]
            