class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        needle_len = len(needle)

        for i in range(0, len(haystack) - needle_len + 1):
            if haystack[i : i + needle_len] == needle:
                return i
        
        return -1
        
        
        # if needle in haystack:
        #     return haystack.find(needle)
        
        # else:
        #     return -1