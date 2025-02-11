class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ms = []

        for w1, w2 in zip(word1, word2):
            ms.append(w1 + w2)
        
        ms.append(word1[len(word2): ])
        ms.append(word2[len(word1): ])

        return ''.join(ms)