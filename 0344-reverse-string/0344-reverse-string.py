class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L, R = 0, len(s) - 1

        while L < R:
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1









    #     left, right = 0, len(s) - 1
    #     while left < right:
    #         s[left], s[right] = s[right], s[left]
    #         left += 1
    #         right -= 1

    #    # return s.reverse()