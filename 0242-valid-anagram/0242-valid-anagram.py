class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Approach 1: O(nlogn)
        # s = list(s)
        # t = list(t)
        # s.sort()
        # t.sort()
        # return s == t
    
        # Approach 2: O(n)
        hashmap = {}
        for i in range(len(t)):
            hashmap[t[i]] = hashmap.get(t[i], 0) + 1
            hashmap[s[i]] = hashmap.get(s[i], 0) - 1
        for char in hashmap:
            if hashmap[char] != 0:
                return False
        return True
            
        
            