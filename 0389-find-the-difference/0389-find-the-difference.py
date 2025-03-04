class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = {}

        for i in t:
            res[i] = res.get(i, 0) + 1

        for j in res:
            if res[j] != s.count(j):
                return j