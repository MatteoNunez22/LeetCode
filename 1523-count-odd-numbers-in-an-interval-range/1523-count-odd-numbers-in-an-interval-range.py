class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        l = (high - low + 1)
        
        if l % 2 == 0:
            return l // 2
        elif low % 2 == 1:
            return (l // 2) + 1
        else:
            return l // 2