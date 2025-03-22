class Solution:
    def countEven(self, num: int) -> int:
        
        even_digit_sums = 0

        for n in range(1, num + 1):

            digit = n
            summ = 0

            while digit:
                summ += digit % 10
                digit //= 10
            
            if summ % 2 == 0:
                even_digit_sums += 1
        
        return even_digit_sums
