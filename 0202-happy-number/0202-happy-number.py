class Solution:
    def isHappy(self, n: int) -> bool:
        
        s = str(n)
        next = 0

        p1 = 0 
        count = 0
        while next != 1 and count < 10:
            
            next = 0
            for v in s:
                next += int(v)*int(v)
            count += 1
            print(next)
            s = str(next)

                
        if next == 1:
            return True
        
        return False

            