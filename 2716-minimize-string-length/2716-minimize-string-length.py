class Solution:
    def minimizedStringLength(self, s: str) -> int:
        
        res = {}

        for i in s:

            if i not in res:
                res[i] = 1
            
        return (len(res))