class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # low = 0
        # high = len(nums) - 1

        # while low <= high:
        #     mid = low + (high - low) // 2

        if target in nums:
            return nums.index(target)
        else:
            return -1