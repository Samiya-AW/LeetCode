class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_b = 0
        close_b = 0
        stack = []

        for i in s:
            
            if i == "(" and open_b < 1:
                open_b += 1
            
            elif i == "(" and open_b > 0:
                stack.append(i)
                open_b += 1
                
            elif i == ")":
                close_b += 1

                if open_b == close_b:
                    open_b = 0
                    close_b = 0
                else:
                    stack.append(i)

        return ''.join(stack)