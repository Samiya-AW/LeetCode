class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        
        count_s = {}

        for c in s:
            count_s[c] = count_s.get(c, 0) + 1
        
        max_count = max(count_s.values())

        for char in count_s.keys():
            if count_s[char] != max_count:
                return False
        
        return True
