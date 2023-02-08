class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        
        dp = []
        
        def dfs(idx):
            if idx in dp:
                return False
            
            if idx == n:
                return True
            
            for word in wordDict:
                l = len(word)
                if idx + l <= n and s[idx:idx+l] == word:
                    if dfs(idx+l):
                        return True
            dp.append(idx)
            return False
        
        return dfs(0)