class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = 0

        for left in range(len(nums)):
            for right in range((left + 1), len(nums)):
                if nums[left] == nums[right]:
                    goodPairs += 1
        
        return goodPairs