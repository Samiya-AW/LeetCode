class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = {}                    
        for n in range(len(nums)):      
            for i in nums[n]:
                counter[i] = counter.get(i, 0) + 1
        
        result = []
        nums_len = len(nums)

        for num in counter.keys():
            if counter[num] == nums_len:
                result.append(num)
        
        return sorted(result)