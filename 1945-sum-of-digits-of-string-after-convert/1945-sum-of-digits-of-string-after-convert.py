class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        str_to_digit = 0

        for a in s:
            a_pos = alphabets.index(a) + 1

            while a_pos:
                str_to_digit = (str_to_digit * 10) + (a_pos % 10)
                a_pos //= 10
        
        for d in range(k):
            summ = 0

            while str_to_digit:
                summ += str_to_digit % 10
                str_to_digit //= 10
            
            str_to_digit = summ

        return summ