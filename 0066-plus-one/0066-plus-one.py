class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        d=map(str, digits)
        d = int(''.join(d))
        d += 1
        d = str(d)
        d = list(d)
        d=map(int, d)
        
        print(d)
        print(type(d))
        
        return d
