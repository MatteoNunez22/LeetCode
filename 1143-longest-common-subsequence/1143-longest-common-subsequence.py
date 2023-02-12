class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # My way: O(n * m), O(min(n,m))
        # n, m = len(text1), len(text2)
        # if len(text1) < len(text2):
        #     text1, text2 = text2, text1
        #     n, m = m, n
        # botRow = [0] * (m + 1)
        # for i in range(n - 1, -1, -1):
        #     currRow = [0] * (m + 1)
        #     for j in range(m - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             currRow[j] = 1 + botRow[j+1]
        #         else:
        #             currRow[j] = max(currRow[j+1], botRow[j])
        #     botRow = currRow
        # return botRow[0]
    
        # Neetcode's way: 
        n, m = len(text1), len(text2)
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[0][0]
        