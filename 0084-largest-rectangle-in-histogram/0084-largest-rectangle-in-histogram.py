class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i, h in enumerate(heights):
            # print("i:", i)
            idx = i
            while stack and stack[-1][-1] > h:
                prev_i, prev_h = stack.pop()
                # print(prev_i, prev_h)
                maxArea = max((i - prev_i)*prev_h, maxArea)
                idx = prev_i
            stack.append((idx, h))
            # print(stack)
            
        while stack:
                prev_i, prev_h = stack.pop()
                # print(prev_i, prev_h)
                maxArea = max((len(heights) - prev_i)*prev_h, maxArea)
        
        return maxArea
                