class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP: O(m * n), O(n)
        botRow = [1] * n
        
        for i in range(m - 1):
            curRow = [1] * n
            for j in range(n - 2, -1, -1):
                curRow[j] = curRow[j+1] + botRow[j]
            botRow = curRow
        
        return botRow[0]