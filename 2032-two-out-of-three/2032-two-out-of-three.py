class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        result = []
        n1 = set(nums1)
        n2 = set(nums2)
        n3 = set(nums3)

        for i in n1:
            if i in n2 or i in n3:
                result.append(i)
        
        for i in n2:
            if i not in result:
                if i in n1 or i in n3:
                    result.append(i)
        
        for i in n3:
            if i not in result:
                if i in n1 or i in n2:
                    result.append(i)

        return result