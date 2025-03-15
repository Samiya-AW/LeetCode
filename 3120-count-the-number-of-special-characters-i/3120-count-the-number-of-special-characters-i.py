class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        count = 0

        for c in range(0, 26, 1):
            upper = chr(c + 65)
            lower = chr(c + 97)
            if upper in word and lower in word:
                count += 1
        
        return count