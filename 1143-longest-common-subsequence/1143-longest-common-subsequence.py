class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        botRow = [0] * (m + 1)
        
        for i in range(n - 1, -1, -1):
            currRow = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    currRow[j] = 1 + botRow[j+1]
                else:
                    currRow[j] = max(currRow[j+1], botRow[j])
            botRow = currRow
            
        return botRow[0]