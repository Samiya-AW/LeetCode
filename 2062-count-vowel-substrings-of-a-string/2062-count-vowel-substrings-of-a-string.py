class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        vowels = set('aeiou')
        count = 0

        for i in range(len(word)):
            if word[i] not in vowels:
                continue
            
            unique_vowel = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break
                
                unique_vowel.add(word[j])
                if len(unique_vowel) == 5:
                    count += 1
        
        return count