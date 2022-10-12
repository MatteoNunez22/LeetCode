class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left = []
        right = []
        
        freq1 = {}
        freq2 = {}
        for i in range(n-1):
            if s[i] in freq1:
                freq1[s[i]] += 1
            else:
                freq1[s[i]] = 1
            left.append(len(freq1))
            
            if s[n-1-i] in freq2:
                freq2[s[n-1-i]] += 1
            else:
                freq2[s[n-1-i]] = 1
            right.insert(0, len(freq2))
        
        count = 0
        for i in range(n-1):
            if left[i] == right[i]:
                count += 1
        return count
        
            