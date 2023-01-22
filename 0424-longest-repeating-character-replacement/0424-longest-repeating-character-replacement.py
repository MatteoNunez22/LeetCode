class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {'A': 0}
        
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while (r - l + 1) - k > max(count.values()):
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
            
        return res