class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            low, high = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while low < high:
                if nums[i] + nums[low] + nums[high] == 0:
                    result.append([nums[i], nums[low], nums[high]])
                low += 1
                high -= 1
        
        return result