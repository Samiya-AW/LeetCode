class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_column = s[0]
        end_column = s[-2]
        result = []

        for column in range(ord(start_column), ord(end_column) + 1):
            current_column = chr(column)
            for row in range(int(s[1]), int(s[-1]) + 1):
                result.append(current_column + str(row))
        
        return result