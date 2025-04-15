class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pairs_count = defaultdict(int)
        res = 0

        for a, b in dominoes:
            key = tuple(sorted((a, b)))
            res += pairs_count[key]
            pairs_count[key] += 1
        
        return res