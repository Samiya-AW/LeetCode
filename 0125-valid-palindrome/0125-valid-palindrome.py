class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 1:
            return True

        new_s = ''
        for c in range(len(s)):
            if s[c].isalpha():
                new_s += s[c].lower()
            elif s[c].isalnum():
                new_s += s[c]

        if len(new_s) == 1:
            return True

        i, j = 0, len(new_s) - 1

        while i <= j:
            if new_s[i] != new_s[j]:
                return False
            i += 1
            j -= 1
        
        return True