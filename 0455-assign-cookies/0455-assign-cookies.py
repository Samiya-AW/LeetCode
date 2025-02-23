class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        content = 0
        for i in range(len(g)):
            j = i
            while j < len(s):
                if s[j] >= g[i]:
                    content += 1
                    break
                else:
                    j += 1
        return content