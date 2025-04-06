class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_str = {}

        for word in list1:
            if word in list2:
                common_str[word] = list1.index(word) + list2.index(word)
        
        min_indx_sum = min(common_str.values())
        res = [k for k, v in common_str.items() if v == min_indx_sum]
        
        return res