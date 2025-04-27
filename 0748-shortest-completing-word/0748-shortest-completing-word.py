class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words = sorted(words, key = len)
        licensePlate = licensePlate.lower()
        licensePlate_count = {}
        
        for letter in licensePlate:
            if letter.isalpha():
                licensePlate_count[letter] = licensePlate_count.get(letter, 0) + 1
        
        def is_completing_word(word):
            word_counter = Counter(word)

            for char, count in licensePlate_count.items():
                if word_counter[char] < count:
                    return False
            
            return True

        for word in words:
            if is_completing_word(word):
                return word