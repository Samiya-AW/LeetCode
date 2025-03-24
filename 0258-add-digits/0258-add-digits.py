class Solution:
    def addDigits(self, num: int) -> int:
        
        if len(str(num)) == 1:
            return num

        def get_next_number(num):
            summ = 0
            while num:
                summ += num % 10
                num //= 10
            
            return summ

        while len(str(num)) > 1:
            num = get_next_number(num)
            if len(str(num)) == 1:
                return num