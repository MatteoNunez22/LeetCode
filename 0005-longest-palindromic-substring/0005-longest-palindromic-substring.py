class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        def expand(l, r):
            while(l>=0 and r<n and s[l]==s[r]):
                l -= 1
                r += 1
            return r-l-1    # (r-1)-(l+1)+1
        
        start, end = 0, 0
        for i in range(n):
            length1 = expand(i, i)
            length2 = expand(i, i+1)
            length = max(length1, length2)
            if length > end-start+1:
                start = i - (length-1)//2
                end = i + length//2
                
        return s[start:end+1]
                
