class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char_map = {}
        
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in char_map and char_map[c] >= l:
                l = char_map[c] + 1
            char_map[c] = r
            max_length = max(max_length, r - l + 1)
            
        return max_length
            
                
                