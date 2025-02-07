class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        triplets = 0

        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                if nums[j] - nums[i] != diff:
                    j += 1
                else:
                    while k > j:
                        if nums[k] - nums[j] == diff:
                            triplets += 1
                        k -= 1
        return triplets