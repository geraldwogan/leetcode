class Solution:
    def reverseWords(self, s: str) -> str:
        
        slist = s.split(' ')
        print(slist)
        slist = [s.strip() for s in slist]
        print(slist)
        slist = list(filter(None, slist))
        print(slist)

        start = 0
        end = len(slist)-1
        
        
        while start < end:
            print(start)
            print(end)
            if start < end:
                slist[start], slist[end] = slist[end], slist[start]
                start += 1
                end -= 1
            
        return ' '.join(slist)
            
        