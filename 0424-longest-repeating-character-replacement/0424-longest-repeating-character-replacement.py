class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def isValid(l, r, count) -> bool:
            return (r - l + 1) - k <= max(count.values())
        
        res = 0
        l = 0
        count = {'A': 0}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while not isValid(l, r, count):
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            res = max(res, r - l + 1)
            
        return res