class Solution:
    def calculate(self, s: str) -> int:
        curr, ans, op = 0, 0, '+'
        s += '+'
        stk = []
        for i in range(len(s)):
            if s[i].isdigit():
                curr = curr * 10 + int(s[i])
            elif s[i] == ' ':
                continue
            else:
                if op == '+':
                    stk.append(curr)
                elif op == '-':
                    stk.append(-curr)
                elif op == '*':
                    num = stk.pop()
                    stk.append(num * curr)
                else:
                    num = stk.pop()
                    stk.append(int(num / curr))
                curr = 0
                op = s[i]
        ans = sum(stk)
        return ans