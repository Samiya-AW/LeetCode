class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_hash = {}

        for n1 in nums1:
            if n1 not in nums1_hash:
                nums1_hash[n1] = 1
            else:
                nums1_hash[n1] += 1

        result = []

        for n2 in nums2:
            if n2 in nums1_hash.keys() and nums1_hash[n2] > 0:
                result.append(n2)
                nums1_hash[n2] -= 1
        
        return result