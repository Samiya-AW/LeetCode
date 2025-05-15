class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        pairs_count = 0
        
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums):
                if abs(nums[i] - nums[j]) == k:
                    pairs_count += 1
                j += 1
        
        return pairs_count