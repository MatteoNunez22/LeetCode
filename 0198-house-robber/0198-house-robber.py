class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
    
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        maxLoot = [0] * n
        maxLoot[0] = nums[0]
        maxLoot[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            maxLoot[i] = max(nums[i] + maxLoot[i-2], maxLoot[i-1])
        
        
        return maxLoot[-1]
    