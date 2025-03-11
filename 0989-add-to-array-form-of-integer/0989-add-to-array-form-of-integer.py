class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1 = 0

        for n in num:
            num1 = (num1 * 10) + n
        
        add = num1 + k

        res = []

        while add > 0:
            res.append(add % 10)
            add //= 10
        
        res = res[::-1]

        return res