class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = s.lower()
        s = [x for x in s if x.isalnum()]
        s = ''.join(s)
        # print(s)
        
        # two pointers
        p1 = 0
        p2 = len(s)-1
        
        while p1<p2:
            if s[p1] != s[p2]:
                return False
            p1+=1
            p2-=1
            
        return True
        
        