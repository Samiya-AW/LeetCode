class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Solution using Hash Table
        # count = {}
        # n = len(nums)
        # res = []
        # for i in nums:
        #     count[i] = 1 + count.get(i, 0)

        # for j in range(1, n + 1):
        #     if j not in count:
        #         res.append(j)
        
        # return res

        # Solution using Array

        for n in nums:
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)

        return res