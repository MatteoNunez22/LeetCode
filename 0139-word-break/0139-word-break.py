class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Recursive DP: O(n*m*n), O(n)
        # n = len(s)
        # dp = []
        # def dfs(idx):
        #     if idx in dp:
        #         return False
        #     if idx == n:
        #         return True
        #     for word in wordDict:
        #         l = len(word)
        #         if idx + l <= n and s[idx:idx+l] == word:
        #             if dfs(idx+l):
        #                 return True
        #     dp.append(idx)
        #     return False
        # return dfs(0)
    
        # Iterative DP: O(n*m*n), O(n)
        n = len(s)
        dp = [True] * (n+1)
        
        for i in range(n-1, -1, -1):
            for word in wordDict:
                l = len(word)
                if i + l <= n and s[i:i+l] == word and dp[i+l]:
                    dp[i] = True
                    break
                dp[i] = False
            
        return dp[0]
        