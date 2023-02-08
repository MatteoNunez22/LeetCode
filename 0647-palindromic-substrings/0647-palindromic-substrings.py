class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        if n == 1:
            return 1
        
        def expand(l, r):
            count = 0 
            while (l >= 0 and r < n and s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            return count
        
        totalCount = 0
        
        for i in range(n):
            totalCount += expand(i, i)
            totalCount += expand(i, i + 1)
            
        return totalCount