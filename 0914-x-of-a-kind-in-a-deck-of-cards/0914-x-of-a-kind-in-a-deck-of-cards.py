class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        deck_count = Counter(deck)
        N = len(deck)

        for X in range(2, N + 1):
            if N % X == 0:
                if all(val % X == 0 for val in deck_count.values()):
                    return True
        
        return False