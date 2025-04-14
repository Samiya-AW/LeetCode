class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        repeated_num_count = len(nums) // 2

        for i in nums:
            count = nums.count(i)
            if count == repeated_num_count:
                return i