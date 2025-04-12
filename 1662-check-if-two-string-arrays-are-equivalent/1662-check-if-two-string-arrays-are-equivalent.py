class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        concatenated_word1 = ''
        concatenated_word2 = ''

        for w1 in word1:
            concatenated_word1 += w1
        
        for w2 in word2:
            concatenated_word2 += w2
        
        return concatenated_word1 == concatenated_word2