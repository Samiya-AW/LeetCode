class Solution:
    def reverseWords(self, s: str) -> str:

        # Solution using Slicing

        s = s + ' '
        res = ''
        start = 0
        for c in range(len(s)):
            if s[c] == ' ':
                res += s[start : c][: : -1] + ' '
                start = c + 1
        
        return res.rstrip()

        # Solution without Slicing

        # res = ''
        # word = ''

        # for c in s:
        #     if c != ' ':
        #         word = c + word
        #     else:
        #         res += word + ' '
        #         word = ''
        # res += word
        # return res


       