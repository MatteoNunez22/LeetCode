class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_map = {}
        
        l = 0
        for r in range(len(s)):
            if s[r] in char_map and char_map[s[r]] >= l:
                l = char_map[s[r]] + 1
            char_map[s[r]] = r
            res = max(res, r - l + 1)
            
        return res
            
                
                