class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        if len(nums) == 1:
            return nums[0]

        while l <= r:
            mid = r + (l - r) // 2

            if mid == 0 and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid == n - 1 and nums[n - 1] != nums[n - 2]:
                return nums[mid]

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid % 2 == 0:
                if nums[mid] == nums[mid - 1]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1

                else:
                    r = mid - 1