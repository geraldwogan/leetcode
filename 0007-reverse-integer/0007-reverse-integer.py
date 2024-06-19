class Solution:
    def reverse(self, x: int) -> int:
        
        s = ''
        if x < 0:
            s = str(x*-1)
        else:
            s = str(x)
        
        # print(s)
        
        s=''.join((list(reversed(s))))
        # print(s)
        s=int(s)
        
        if s > 2147483648:
            return 0

        return s if x > 0 else s*-1