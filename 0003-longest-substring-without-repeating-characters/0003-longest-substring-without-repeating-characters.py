class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # My method: O(n), O(n)
        # res = 0
        # char_map = {}
        # l = 0
        # for r in range(len(s)):
        #     if s[r] in char_map and char_map[s[r]] >= l:
        #         l = char_map[s[r]] + 1
        #     char_map[s[r]] = r
        #     res = max(res, r - l + 1)
        # return res
            
        # Neetcode's method: O(n), O(n)
        res = 0
        char_set = set()
        
        l = 0
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
            
        return res
                
                