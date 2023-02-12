class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Slow Recursive + Memo: O(n^2), O(n)
        # n = len(nums)
        # dp = set()
        # def dfs(i):
        #     if i == n - 1:
        #         return True
        #     if i in dp or nums[i] == 0:
        #         return False
        #     for j in range(nums[i] + i, i, -1):
        #         if j < n and dfs(j):
        #             return True
        #     dp.add(i)
        #     return False
        # return dfs(0)
        
        # Greedy: O(n), O(1)
        n = len(nums)
        lastIdx = n - 1
        
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= lastIdx:
                lastIdx = i
            
        return lastIdx == 0
        