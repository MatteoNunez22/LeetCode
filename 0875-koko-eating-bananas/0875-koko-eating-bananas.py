class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        res = r
        
        while l <= r:
            k = l + (r - l) // 2
            
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
                
            if hours > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1
            
        return res