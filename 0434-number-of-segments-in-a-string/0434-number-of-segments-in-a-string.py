class Solution:
    def countSegments(self, s: str) -> int:

        segments = []
        word = ''

        for c in s:
            if c != ' ' and c != '':
                word += c
            else:
                if word != '':
                    segments.append(word)
                    word = ''
        
        if word != '':
            segments.append(word)
        
        return len(segments)

        # segments = s.split()

        # return len(segments)