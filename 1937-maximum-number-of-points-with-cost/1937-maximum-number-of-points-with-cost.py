class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points) # rows
        n = len(points[0])  # columns
        
        # One row
        if m == 1:
            return max(points[0])
        # One column
        if n == 1:
            return sum(x[0] for x in points)
        
        # Iterate rows
        prev = points[0]
        for i in range(m-1):
            # Left to right max
            left = [prev[0]] + [0]*(n-1)
            for j in range(1,n):
                left[j] = max(prev[j], left[j-1]-1)
            
            # Right to left max
            right = [0]*(n-1) + [prev[-1]]
            for j in range(n-2, -1, -1):
                right[j] = max(prev[j], right[j+1]-1)
                
            # Populate curr array
            curr = [0]*n
            for j in range(0,n):
                curr[j] = points[i+1][j] + max(left[j], right[j])
            
            # Update prev array
            prev = curr[:]
            
        return max(prev)