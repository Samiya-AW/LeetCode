class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = ['1']

        if n == 1:
            return answer

        for i in range(2, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        
        return answer