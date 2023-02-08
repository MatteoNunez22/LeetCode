class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        if n == 1:
            return 1 if s[0] != "0" else 0
        
        countMap = { n : 1 }
        
        def ways(idx):
            if idx in countMap:
                return countMap[idx]
            
            if idx >= n or s[idx] == "0":
                return 0
            
            count = ways(idx + 1)
            if idx + 1 < n and int(s[idx:idx+2]) <= 26:
                count += ways(idx + 2)
            
            countMap[idx] = count
            
            return count
        
        return ways(0)
        