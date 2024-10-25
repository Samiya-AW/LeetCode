class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res, count_dict = [], {}
        s1 = s1.split()
        s2 = s2.split()

        for s in s1:
            count_dict[s] = count_dict.get(s, 0) + 1

        for s in s2:
            count_dict[s] = count_dict.get(s, 0) + 1

        for counter in count_dict:
            if count_dict[counter] == 1:
                res.append(counter)

        return res