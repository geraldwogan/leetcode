class Solution:
    def reverseWords(self, s: str) -> str:
        slist = s.strip().split(' ')
        # slist = s.split(' ')
        slist = list(filter(None, slist))

        start = 0
        end = len(slist)-1
        
        while start < end:
            if start < end:
                slist[start], slist[end] = slist[end], slist[start]
                start += 1
                end -= 1
            
        return ' '.join(slist)
            
        