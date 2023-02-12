class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = set()
        
        def dfs(i):
            if i == n - 1:
                return True
            
            if i in dp or nums[i] == 0:
                return False
   
            for j in range(nums[i] + i, i, -1):
                if j < n and dfs(j):
                    return True
            dp.add(i)
            return False
            
        return dfs(0)