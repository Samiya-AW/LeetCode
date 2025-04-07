class Solution:
    def countSegments(self, s: str) -> int:
        
        if s == '':
            return 0

        s = s + ' '
        seg_count = 0

        for c in s:
            if c == ' ':
                seg_count += 1
        
        return seg_count