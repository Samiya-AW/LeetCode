class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hsh = {}

        for i in nums:
            hsh[i] = 1 + hsh.get(i, 0)
            if hsh[i] == 2:
                return True
            
        return False

        # # Brute Force Solution
        # nums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        
        # return False