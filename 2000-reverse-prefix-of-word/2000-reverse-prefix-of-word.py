class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        if ch not in word:
            return word
        
        ch_ind = word.index(ch)
        reverse_word = []

        for w in range(ch_ind, -1, -1):
            reverse_word.append(word[w])
        
        return ''.join(reverse_word) + word[ch_ind + 1:]