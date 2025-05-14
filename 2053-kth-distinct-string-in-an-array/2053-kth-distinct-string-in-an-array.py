class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinct = []
        
        for char in arr:
            if arr.count(char) == 1:
                distinct.append(char)
        
        if len(distinct) < k:
            return ""
        else:
            return distinct[k - 1]