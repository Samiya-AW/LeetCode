class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        count = [0] * 10

        for c in num:
            count[int(c)] += 1
        
        for i in range(n):
            if count[i] != int(num[i]):
                return False
        
        return True