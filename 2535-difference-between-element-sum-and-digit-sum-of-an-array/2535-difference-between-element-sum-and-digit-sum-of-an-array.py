class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        ele_sum, dig_sum = 0, 0

        for e in nums:
            ele_sum += e
        
        for d in range(len(nums)):
            cur_num = str(nums[d])
            for s in cur_num:
                dig_sum += int(s)
        
        return abs(ele_sum - dig_sum)