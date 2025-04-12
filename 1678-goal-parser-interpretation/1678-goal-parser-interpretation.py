class Solution:
    def interpret(self, command: str) -> str:
        
        result = ''
        for c in range(len(command)):
            if command[c] == 'G':
                result += command[c]

            elif command[c] == 'a' and command[c + 1] == 'l':
                result += command[c] + command[c + 1]
            
            elif command[c] == '(' and command[c + 1] == ')':
                result += 'o'
        
        return result