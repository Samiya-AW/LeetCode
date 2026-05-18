class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # duplicates = {}
        # for i in nums:
        #     duplicates[i] = duplicates.get(i, 0) + 1
        
        # for d in duplicates.values():
        #     if d > 1:
        #         return True
        
        # return False

        # Solution 2

        duplicates = set()
        for i in nums:
            if i not in duplicates:
                duplicates.add(i)
            else:
                return True
        
        return False