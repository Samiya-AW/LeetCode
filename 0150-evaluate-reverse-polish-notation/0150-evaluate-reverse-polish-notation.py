class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == '+':
                stack.append(stack.pop() + stack.pop())

            elif i == '-':
                a, g = stack.pop(), stack.pop()
                stack.append(g - a)

            elif i == '*':
                stack.append(stack.pop() * stack.pop())

            elif i == '/':
                a, g = stack.pop(), stack.pop()
                stack.append(int(g / a))

            else:
                stack.append(int(i))

        return stack[-1]