class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {'(': ')', '{': '}', '[': ']'}
        
        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if not stack or pair[stack[-1]] != c:
                    return False
                stack.pop()
        
        return len(stack) == 0
                    