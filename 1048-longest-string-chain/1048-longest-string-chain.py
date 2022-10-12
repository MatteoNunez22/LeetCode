class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        
        dp = {}
        res = 0
        for word in words:
            dp[word] = 1
            
            for i in range(len(word)):
                pred = word[:i] + word[i+1:]
                
                if pred in dp and dp[word] < dp[pred] + 1:
                    dp[word] = dp[pred] + 1
                    
            res = max(res, dp[word])
            
        return res