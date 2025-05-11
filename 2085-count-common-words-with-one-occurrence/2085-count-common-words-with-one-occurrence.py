class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # result = 0

        # for word in words1:
        #     if word in words2 and words1.count(word) == 1 and words2.count(word) == 1:
        #         result += 1
        
        # return result

        result = 0
        words1_dict = {}
        
        for w in words1:
            words1_dict[w] = words1_dict.get(w, 0) + 1
        
        for word in words1_dict.keys():
            if word in words2 and words1_dict[word] == 1 and words2.count(word) == 1:
                result += 1
        
        return result