class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        if n == 1:
            return s
        
        def expand(l, r):
            while (l >= 0 and r < n and s[l] == s[r]):
                    l -= 1
                    r += 1
            return r - l - 1    # (r-1) - (l+1) + 1
        
        start, end = 0, 0
        
        for i in range(n):
            l1 = expand(i,i)
            l2 = expand(i,i+1)
            length = max(l1, l2)
            if length > end - start + 1:
                start, end = i - (length-1)//2, i + length//2
            
        return s[start:end+1]