class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        
        for num, i in enumerate(range(1, n+1), start=1):
            if num % 3 == 0 and num % 5 == 0:
                answer.append('FizzBuzz') 
            elif num % 3 == 0:
                answer.append('Fizz') 
            elif num % 5 == 0:
                answer.append('Buzz') 
            else:
                answer.append(str(i))
                
        return answer