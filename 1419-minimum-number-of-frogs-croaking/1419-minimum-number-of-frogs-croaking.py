class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        numFrogs = 0
        
        c = 0
        r = 0
        o = 0
        a = 0
        k = 0
        for ch in croakOfFrogs:
            if ch not in 'croak':
                return -1
            
            if ch == 'c':
                c += 1
                numFrogs = max(numFrogs, c - k)
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            else:
                k += 1
                
            if not c >= r >= o >= a >= k:
                return -1
            
        if c == k:
            return numFrogs
        else:
            return -1