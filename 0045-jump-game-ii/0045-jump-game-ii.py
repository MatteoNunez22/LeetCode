class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP
        # n = len(nums)
        # dp = [0] * n
        # for i in range(n - 2, -1, -1):
        #     if nums[i] == 0:
        #         dp[i] = -1
        #         continue
        #     minJump = float("inf")
        #     for j in range(i + 1, min(i + 1 + nums[i], n)):
        #         if dp[j] != -1:
        #             minJump = min(minJump, dp[j])
        #     dp[i] = minJump + 1
        # return dp[0]
    
        # Greedy
        jumps = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            maxJump = 0
            for i in range(l, r + 1):
                maxJump =  max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            jumps += 1
        
        return jumps
        
            