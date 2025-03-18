class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        self_dividing = []
       
        for num in range(left, right + 1):
            n = num
            num_list = []
            while n != 0:
                num_list.append(n % 10)
                n //= 10
            
            divide_count = 0

            if 0 not in num_list:

                for d in num_list:
                    if num % d == 0:
                        divide_count += 1
                
                if divide_count == len(num_list):
                    self_dividing.append(num)
        
        return self_dividing