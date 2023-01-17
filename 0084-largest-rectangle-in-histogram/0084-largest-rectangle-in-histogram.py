class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][-1] > h:
                prev_i, prev_h = stack.pop()
                maxArea = max((i - prev_i)*prev_h, maxArea)
                idx = prev_i
            stack.append((idx, h))
            
        while stack:
            prev_i, prev_h = stack.pop()
            maxArea = max((len(heights) - prev_i)*prev_h, maxArea)
        
        return maxArea
                