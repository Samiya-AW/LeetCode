class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        summ = 0
        n_list = []

        while n:
            n_list.append(n % 10)
            n //= 10
        n_list = n_list[::-1]

        for digit in range(len(n_list)):
            if digit % 2 == 0:
                summ += n_list[digit]
            else:
                summ -= n_list[digit]
        
        return summ
