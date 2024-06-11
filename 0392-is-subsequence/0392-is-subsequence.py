class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
#         idx = 0
#         for i in range(len(s)):
#             found = False
#             for j in range(len(t)):
#                 if s[i] == t[j] and idx <= j:
#                     print(f'found {s[i]}')
#                     idx = j
#                     found = True
#                     front = t[:j]   # up to but not including n
#                     back = t[j+j:]  # n+1 through end of string
#                     t = front + back
#                     continue
                    
#             if found == False:
#                 return False
#             else:
#                 break
#         return True
        
        for i in range(len(s)):
            print(f'searching for {s[i]}')
            found = False

            for j in range(len(t)):
                print(f'checking {t[j]}')
                if s[i] == t[j]:
                    print(f'found')
                    t = t[j+1:]
                    print(f'reduced to {t}')
                    found = True
                    break 
           
        
        
            if found == False:
                return False
        return True
                    