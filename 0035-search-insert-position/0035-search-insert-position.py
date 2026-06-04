class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for n in range(len(nums)):
            if nums[n] == target:
                return n
            elif nums[n] > target:
                return n
        
        return n + 1