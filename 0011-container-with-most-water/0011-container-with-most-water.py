class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        l = 0
        r = len(height) - 1
        
        while l < r:
            water = min(height[l], height[r]) * (r - l)
            # print(f"res: {res}")
            # print(f"(l, r): {l}, {r}")
            # print(f"height(l, r): {height[l]}, {height[r]}")
            # print(f"water area: {water}")
            res = max(water, res)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res