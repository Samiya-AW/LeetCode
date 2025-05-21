class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_dict = {}

        for n1 in nums1:
            nums1_dict[n1] = nums1_dict.get(n1, 0) + 1
        
        for n2 in nums2:
            if nums1_dict.get(n2, 0) != 0:
                result.append(n2)
                nums1_dict[n2] -= 1
    
        return result