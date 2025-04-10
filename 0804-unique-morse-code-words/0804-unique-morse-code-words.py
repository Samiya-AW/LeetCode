class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_transformation = []

        for w in range(len(words)):
            morse_word = ''
            for letter in words[w]:
                morse_word += morse_code[ord(letter) - 97]
            if morse_word not in morse_transformation:
                morse_transformation.append(morse_word)
        
        return len(morse_transformation)