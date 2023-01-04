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
            if t[i] in hashmap:
                hashmap[t[i]] += 1
            else:
                hashmap[t[i]] = 1
            if s[i] in hashmap:
                hashmap[s[i]] -= 1
            else:
                hashmap[s[i]] = -1
        for char in hashmap:
            if hashmap[char] != 0:
                return False
        return True
            
        
            