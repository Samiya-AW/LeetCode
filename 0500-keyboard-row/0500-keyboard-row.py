class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = 'qwertyuiop'
        second_row = 'asdfghjkl'
        third_row = 'zxcvbnm'

        res = []

        for word in words:
            w = word.lower()
            if len(set(first_row + w)) == len(first_row) or len(set(second_row + w)) == len(second_row) or len(set(set(third_row + w))) == len(third_row):
                res.append(word)

        return res