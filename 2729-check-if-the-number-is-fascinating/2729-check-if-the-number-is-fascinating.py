class Solution:
    def isFascinating(self, n: int) -> bool:
        n_2 = 2 * n
        n_3 = 3 * n

        concatenated_num = str(n) + str(n_2) + str(n_3)

        digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for d in digits:
            if d not in concatenated_num or concatenated_num.count(d) > 1:
                return False
        
        return True

