class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = {}
        # arr = sorted(nums)
        n = len(nums)
        res = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for j in range(1, n + 1):
            if j not in count:
                res.append(j)
        
        return res