class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        for char in t:
            count_s = s.count(char)
            count_t = t.count(char)
            if count_s != count_t:
                return char

        # Solution using Hash Table
        # res = {}

        # for i in t:
        #     res[i] = res.get(i, 0) + 1

        # for j in res:
        #     if res[j] != s.count(j):
        #         return j