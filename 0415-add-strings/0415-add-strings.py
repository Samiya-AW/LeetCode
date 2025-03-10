class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        if num1 == '0' and num2 == '0':
            return '0'

        n1 = 0
        n2 = 0
        
        for digit1 in num1:
            n1 = n1 * 10 + (ord(digit1) - 48)
        
        for digit2 in num2:
            n2 = n2 * 10 + (ord(digit2) - 48)
        
        add = n1 + n2

        res = []
        
        while add > 0:
            num = add % 10
            res.append(chr(num + 48))
            add //= 10
        
        res.reverse()

        return ''.join(res)