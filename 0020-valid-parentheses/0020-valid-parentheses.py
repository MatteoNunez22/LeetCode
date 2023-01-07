class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            '(': ")",
            '{': "}",
            '[': "]"
        }
        
        for c in s:
            if c in pair:
                stack.append(c)
            else:
                if len(stack) == 0 or pair[stack.pop(-1)] != c:
                    return False
        
        return len(stack) == 0
           