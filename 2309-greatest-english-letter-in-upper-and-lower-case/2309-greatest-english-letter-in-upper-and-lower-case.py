class Solution:
    def greatestLetter(self, s: str) -> str:
        
        for c in range(25, -1, -1):
            upper = chr(c + 65)
            lower = chr(c + 97)
            if upper in s and lower in s:
                return upper
        
        return ''