class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # My method: O(26n), O(n)
        # res = 0
        # count = {}
        # l = 0
        # for r in range(len(s)):
        #     count[s[r]] = count.get(s[r], 0) + 1
        #     while (r - l + 1) - k > max(count.values()):
        #         count[s[l]] -= 1
        #         l += 1
        #     res = max(res, r - l + 1)
        # return res
        
        # Neetcode's method: O(n), O(n)
        res = 0
        count = {}
        maxfreq = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxfreq = max(maxfreq, count[s[r]])
            while (r - l + 1) - k > maxfreq:
                print(l, r)
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res