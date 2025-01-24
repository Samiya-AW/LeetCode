class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_arr = []
        temp = 0

        for i in range(len(nums)):
            temp += nums[i]
            result_arr.append(temp)
        
        return result_arr