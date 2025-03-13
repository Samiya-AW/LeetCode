class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_count = Counter(s)
        target_count = Counter(target)

        res = len(s)

        for c in target_count:
            res = min(res, s_count[c] // target_count[c])

        return res