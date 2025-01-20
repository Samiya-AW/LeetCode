class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count = {}

        for i in s:
            count[i] = 1 + count.get(i, 0)
            if count[i] == 2:
                return i