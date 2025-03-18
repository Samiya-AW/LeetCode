class Solution:
    def countDigits(self, num: int) -> int:
        
        num_list = []
        n = num

        while n != 0:
            num_list.append(n % 10)
            n //= 10
        
        divide_count = 0

        for d in range(len(num_list)):
            if num % num_list[d] == 0:
                divide_count += 1
        
        return divide_count