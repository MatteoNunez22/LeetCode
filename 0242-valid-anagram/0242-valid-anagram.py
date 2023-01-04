class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        
        s = list(s)
        t = list(t)
        
        for char in t:
            if not char in s:
                return False
            s.remove(char)
            
        return len(s) == 0