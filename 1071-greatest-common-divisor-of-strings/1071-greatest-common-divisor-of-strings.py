class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # base case
        if(str1==str2):
            return str1
        
        divs = []
        
        for i, val in enumerate(str2):
            for j, val in enumerate(str2):
                div = str2[i:j+1]
                if len(div) > 0 and div not in divs:
                    
                    # print(f'start {str2[i:j+1]}')
                   
                    # Attempt 1:
                    # if ((str2[i:j+1] + str2[i:j+1] in str1 and str2[i:j+1] in str2) 
                    # # or (str2[i:j+1] + str2[i:j+1] in str2 and str2[i:j+1] in str1) 
                    # and len(str2[i:j+1])>0
                    # and len(splits[0])==len(splits[-1])
                    # ):
                    
                    # Attempt 2:
                    # splits = str1.split(str2[i:j+1])
                    # print(splits)
                    # if(len(set(splits))==1 and len(splits)!=1 and len(str1)!=len(str2[i:j+1])):
                    
                    # Attempt 3: 
                    if(len(div)*(str1.count(div)) == len(str1) and len(div)*(str2.count(div)) == len(str2) ):
                        # print(f'found :: {str2[i:j+1]}')
                        divs.append(str2[i:j+1])
                        

        print(divs)
        
        return max(divs, key=len) if divs else ""
