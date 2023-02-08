class Solution:
    def rob(self, nums: List[int]) -> int:
        loot1, loot2 = 0, 0
        
        for n in nums:
            maxLoot = max(n + loot1, loot2)
            loot1 = loot2
            loot2 = maxLoot
        
        return loot2
    