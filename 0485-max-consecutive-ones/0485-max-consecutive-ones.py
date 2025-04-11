class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_1s = 0
        max_cons = 0

        for n in nums:
            if n == 1:
                max_1s += 1
            else:
                max_cons = max(max_1s, max_cons)
                max_1s = 0
        max_cons = max(max_1s, max_cons)
        return max_cons