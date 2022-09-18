class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for token in tokens:
            if token.lstrip('-').isdigit():
                 stack.append(int(token))
            else:
                digit2 = stack.pop()
                digit1 = stack.pop()
                if token == '+':
                    stack.append(digit1 + digit2)
                elif token == '-':
                    stack.append(digit1 - digit2)
                elif token == '*':
                    stack.append(digit1 * digit2)
                elif token == '/':
                    stack.append(int(digit1 / digit2))
                
        return stack.pop()
            