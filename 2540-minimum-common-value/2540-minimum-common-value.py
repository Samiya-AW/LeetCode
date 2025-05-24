class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        common_integers = set(nums1) & set(nums2)

        if common_integers:
            return min(common_integers)
    
        return -1