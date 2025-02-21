class Solution:
    def maxDepth(self, s: str) -> int:
        
        count, max_depth = 0, 0

        for i in s:
            if i == '(':
                count += 1
                max_depth = max(max_depth, count)
            
            if i == ')':
                count -= 1
        
        return max_depth