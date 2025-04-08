class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 1:
            return False

        divisor_sum = 1             # 1 is always a divisor
        sqrt_num = int(num ** 0.5)
        
        for d in range(2, sqrt_num + 1):
            if num % d == 0:
                divisor_sum += d
                if d != num // d:   # Avoid square root twice num is a perfect square root
                    divisor_sum += num // d
        
        return (divisor_sum == num)