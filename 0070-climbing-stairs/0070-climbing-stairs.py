class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n

        a = 2
        b = 3
        
        for i in range(n-3):
            c = a + b
            a = b
            b = c
            
        return b