class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        special_count = 0

        for c in range(0, 26, 1):
            upper = chr(c + 65)
            lower = chr(c + 97)
            if upper in word and lower in word and word.find(lower) < word.find(upper) and word.rfind(lower) < word.find(upper):
                special_count += 1
        
        return special_count