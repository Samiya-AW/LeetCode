class Solution:
    def decodeString(self, s: str) -> str:
        digit = 0
        temp = ''
        stack = []

        for i in s:
            if i.isdigit():
                digit = (digit * 10) + int(i)
            
            elif i == '[':
                stack.append((temp, digit))
                digit = 0
                temp = ''
            
            elif i == ']':
                string, num = stack.pop()
                temp = string + (temp * num)

            else:
                temp += i

        return temp