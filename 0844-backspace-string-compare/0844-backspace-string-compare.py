class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk_s, stk_t = [], []

        for i in s:
            if stk_s and i == '#':
                stk_s.pop()
            elif i == '#':
                continue
            else:
                stk_s.append(i)

        for j in t:
            if stk_t and j == '#':
                stk_t.pop()
            elif j == '#':
                continue
            else:
                stk_t.append(j)
        
        return (''.join(stk_s) == ''.join(stk_t))