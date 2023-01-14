class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(n_left, n_right):
            if n_left == n_right == n:
                res.append("".join(stack))
                return
            if n_left < n:
                stack.append("(")
                backtrack(n_left + 1, n_right)
                stack.pop()
            
            if n_right < n_left:
                stack.append(")")
                backtrack(n_left, n_right + 1)
                stack.pop()
        
        backtrack(0, 0)
        
        return res
                
                
            