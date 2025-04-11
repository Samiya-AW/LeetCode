class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        
        total_lines = 1
        new_line_width = 0

        for letter in s:
            w = widths[ord(letter) - 97]
            new_line_width += w
            if new_line_width > 100:
                total_lines += 1
                new_line_width = w
        
        return [total_lines, new_line_width]