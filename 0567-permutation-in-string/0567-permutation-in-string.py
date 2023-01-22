class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26
        matches = 0
        
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
            
        for i in range(len(count1)):
            if count1[i] == count2[i]:
                matches += 1
        
        if matches == 26:
            return True
        
        l = 0
        for r in range(len(s1), len(s2)):
            idx = ord(s2[r]) - ord('a')
            count2[idx] += 1
            if count2[idx] == count1[idx]:
                matches += 1
            elif count2[idx] == count1[idx] + 1:
                matches -= 1
               
            idx = ord(s2[l]) - ord('a')
            count2[idx] -= 1
            if count2[idx] == count1[idx]:
                matches += 1
            elif count2[idx] == count1[idx] - 1:
                matches -= 1
            l += 1
            
            if matches == 26:
                return True
            
        return False
            