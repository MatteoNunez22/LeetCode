class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        res = r
        
        while l <= r:
            k = l + (r - l) // 2
            
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
                
            print(l, r, k)
            print(hours)
                
            if hours > h:
                l = k + 1
            else:
                r = k - 1
                res = min(res, k)
            
        return res