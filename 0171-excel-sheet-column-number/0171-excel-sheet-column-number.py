class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber = 0

        for char in columnTitle:
            current_char_num = (ord(char) - ord('A')) + 1
            columnNumber = (columnNumber * 26) + current_char_num
        
        return columnNumber