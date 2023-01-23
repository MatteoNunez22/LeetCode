class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = ""
        minLength = len(s)
        
        tCount = {}
        sCount = {}
        matches = 0
        
        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1
            
        l = 0
        for r in range(len(s)):
            # Complete substring
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            if s[r] in t and sCount[s[r]] == tCount[s[r]]:
                matches += 1
            if matches == len(tCount):
                # Minimize substring
                while s[l] not in t or sCount[s[l]] > tCount[s[l]]:
                    if s[l] in t:
                        sCount[s[l]] -= 1
                    l += 1

                # Check substring length
                if len(s[l:r+1]) <= minLength:
                    minLength = len(s[l:r+1])
                    res = s[l:r+1]
            
                # Move pointers
                sCount[s[l]] -= 1
                l += 1
                matches -= 1
        
        return res