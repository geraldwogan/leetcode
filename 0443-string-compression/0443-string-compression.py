class Solution:
    def compress(self, chars: List[str]) -> int:
        print("=======")
        s = ''
        end = len(chars)
        p1 = 0 
        p2 = 1
        
        while p2 < end:
            if(chars[p1] == chars[p2]): 
                print(f'match: {chars[p1]} == {chars[p2]}')
                p2 +=1 #TODO: Handle tens
            else:
                s += chars[p1] 
                s += str(p2-p1) if p2-p1>1 else ''
                print(s)
                p1 = p2
                
        s += chars[p1] 
        s += str(p2-p1) if p2-p1>1 else ''
        print(p2)
        print(s)
        
        p1 = p2
        
        # r= [*s]
        print(f'chars: {chars}')
        chars.clear()
        print(f'chars: {chars}')

        for i, val in enumerate(s):
            # chars.insert(i, r[i])
            
            # print(f'replace {chars[i]} with {s[i]}')
            print(f'insert {s[i]}')
            chars.insert(i,s[i])
            # print(chars)
        
        # chars = chars[0:-1]
        # print( [*s])
        # chars.clear()
        # chars = [*s]
        print(chars)
        return len(chars)
            