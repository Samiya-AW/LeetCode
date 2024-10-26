class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < abs(a):
                    stack.pop()
                    
                elif stack[-1] == abs(a):
                    stack.pop()
                    break
                    
                else:
                    break

            else: 
                stack.append(a)
        
        return stack