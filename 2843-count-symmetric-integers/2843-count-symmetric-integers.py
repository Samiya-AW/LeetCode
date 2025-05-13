class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0

        for x in range(low, high + 1):
            str_x = str(x)
            if len(str_x) % 2 == 0:
                mid_index = len(str_x) // 2
                first_half = str_x[0 : mid_index]
                last_half = str_x[mid_index : ]
                first_half_sum = 0
                last_half_sum = 0
                for i in first_half:
                    first_half_sum += int(i)
                for j in last_half:
                    last_half_sum += int(j)
                
                if first_half_sum == last_half_sum:
                    result += 1
        
        return result