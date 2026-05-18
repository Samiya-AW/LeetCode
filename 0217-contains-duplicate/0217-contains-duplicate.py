class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicates = {}
        for i in nums:
            duplicates[i] = duplicates.get(i, 0) + 1

        print(duplicates)
        
        for d in duplicates.values():
            if d > 1:
                return True
        
        return False