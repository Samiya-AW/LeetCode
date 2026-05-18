class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers solution

        # Cleaning s
        clean_s = ""
        for ch in s:
            if ch.isalnum():
                clean_s += ch.lower()
        
        # Initialize two pointers

        left = 0
        right = len(clean_s) - 1
        while left <= right:
            if clean_s[left] != clean_s[right]:
                return False
            else:
                left += 1
                right -=1
        return True