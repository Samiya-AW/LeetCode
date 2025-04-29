class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        
        w = 1
        while w < len(words):
            if ''.join(sorted(words[w - 1])) == ''.join(sorted(words[w])):
                words.pop(w)
            else:
                w += 1
        
        return words