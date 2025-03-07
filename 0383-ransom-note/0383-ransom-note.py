class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count_ransomNote = Counter(ransomNote)
        count_magazine = Counter(magazine)

        for char, count in count_ransomNote.items():
            if count_magazine[char] < count:
                return False
        
        return True