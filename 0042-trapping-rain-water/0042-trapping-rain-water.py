class Solution:
    def trap(self, height: List[int]) -> int:
        # Approach 1: Dynamic Programming O(n), O(n)
        # res = 0
        # maxLeft = [0] * len(height)
        # maxRight = [0] * len(height)
        # max_h = height[0]
        # for i in range(len(height)-1):
        #     max_h = max(max_h, height[i])
        #     maxLeft[i] = max_h
        # max_h = height[-1]
        # for i in range(1, len(height))[::-1]:
        #     max_h = max(max_h, height[i])
        #     maxRight[i] = max_h
        # for i in range(len(height)):
        #      res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        # return res
        
        # Approach 2: Two pointers O(n), O(1)
        if len(height) <= 2:
            return 0
        
        res = 0
        l, r = 0, len(height) - 1
        
        water_height = min(height[l], height[r])
        
        while l < r:
            if height[l] < height[r]:
                l += 1
                res += max(water_height - height[l], 0)
            else:
                r -= 1
                res += max(water_height - height[r], 0)
                
            water_height = max(water_height, min(height[l], height[r]))
            
        return res