class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
    
        if n == 1:
            return nums[0]
        
        if n == 2:
            return max(nums[0], nums[1])
        
        loot1, loot2 = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n):
            maxLoot = max(nums[i] + loot1, loot2)
            loot1 = loot2
            loot2 = maxLoot
        
        return maxLoot
    