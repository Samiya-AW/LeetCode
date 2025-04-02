class Solution:
    def possibleStringCount(self, word: str) -> int:
        possible_strings = 1

        for w in range(1, len(word)):
            if word[w] == word[w - 1]:
                possible_strings += 1
        
        return possible_strings