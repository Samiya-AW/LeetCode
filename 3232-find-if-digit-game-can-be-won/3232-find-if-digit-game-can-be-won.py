class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        
        single_digit_sum = 0
        double_digit_sum = 0

        for n in nums:
            if len(str(n)) == 1:
                single_digit_sum += n
            else:
                double_digit_sum += n
        
        if single_digit_sum != double_digit_sum:
            return True
        
        else:
            return False