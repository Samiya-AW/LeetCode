class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        str_to_digit = 0

        for a in s:
            digit = alphabets.index(a) + 1

            while digit:
                str_to_digit = (str_to_digit * 10) + (digit % 10)
                digit //= 10
        
        for d in range(k):
            summ = 0

            while str_to_digit:
                summ += str_to_digit % 10
                str_to_digit //= 10
            
            str_to_digit = summ

        return summ