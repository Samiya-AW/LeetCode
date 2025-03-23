class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        answer = []

        for n in nums:

            for digit in str(n):
                answer.append(int(digit))
    
        return answer