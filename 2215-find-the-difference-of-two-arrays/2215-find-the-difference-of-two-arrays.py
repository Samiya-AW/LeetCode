class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1 = []
        n2 = []

        for i in set(nums1):
            if i not in nums2:
                n1.append(i)

        for j in set(nums2):
            if j not in nums1:
                n2.append(j)
    
        return [n1, n2]