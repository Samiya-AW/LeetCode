class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s + ' '
        res = ''
        start = 0
        for c in range(len(s)):
            if s[c] == ' ':
                res += s[start : c][: : -1] + ' '
                start = c + 1
        
        return res.rstrip()