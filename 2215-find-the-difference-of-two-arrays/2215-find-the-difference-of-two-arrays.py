class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[], []]

        for n1 in nums1:
            if n1 not in nums2 and n1 not in result[0]:
                result[0].append(n1)

        for n2 in nums2:
            if n2 not in nums1 and n2 not in result[1]:
                result[1].append(n2)

        return result