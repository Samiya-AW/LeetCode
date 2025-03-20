class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        str_to_digit = 0

        for a in s:
            str_to_digit = (str_to_digit * 10) + (alphabets.index(a) + 1)
        
        num = str_to_digit

        for d in range(k):
            summ = 0

            while str_to_digit:
                summ += str_to_digit % 10
                str_to_digit //= 10
            
            str_to_digit = summ

        return summ