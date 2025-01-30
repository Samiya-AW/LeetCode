class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for j in count:
            if count[j] == 1:
                return j