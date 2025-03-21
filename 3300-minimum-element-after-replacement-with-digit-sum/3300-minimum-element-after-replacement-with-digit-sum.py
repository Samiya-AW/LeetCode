class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        for n in range(len(nums)):
            digit = nums[n]
            summ = 0

            while digit:
                summ += digit % 10
                digit //= 10

            nums[n] = summ

        return min(nums)        