class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = 'aeiouAEIOU'
       
        slist = list(s)
        
        start = 0
        end = len(s)-1
        
        while start < end:
            print(start)
            print(end)
            while start < len(s) and slist[start] not in vowels:
                start += 1
            while end >= 0 and slist[end] not in vowels:
                end -= 1
            if start < end:
                print(f'swap! {start} for {end}')
                slist[start], slist[end] = slist[end], slist[start]
                start += 1
                end -= 1
        
        return ''.join(slist)
