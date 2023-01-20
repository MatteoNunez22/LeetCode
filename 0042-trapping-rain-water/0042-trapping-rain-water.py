class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        
        l, r = 0, len(height) - 1
        water_height = min(height[l], height[r])
        
        while l < r:
            if height[l] < height[r]:
                l += 1
                water = max(water_height - height[l], 0)
                res += water
            else:
                r -= 1
                water = max(water_height - height[r], 0)
                res += water
            
            water_height = max(water_height, min(height[l], height[r]))
        
        return res