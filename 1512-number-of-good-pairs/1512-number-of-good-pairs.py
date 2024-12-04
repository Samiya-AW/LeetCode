class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # Solution using Hash Table

        res = 0
        count = {}

        for n in nums:
            if n in count:
                res += count[n]
                count[n] += 1

            else:
                count[n] = 1

        return res


        # Solution using two for loops
        
        # goodPairs = 0

        # for left in range(len(nums)):
        #     for right in range((left + 1), len(nums)):
        #         if nums[left] == nums[right]:
        #             goodPairs += 1
        
        # return goodPairs