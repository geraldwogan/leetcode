class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Loop over each letter that needs to be found
        for i in range(len(s)):
            found = False
            # Loop over each letter that is a potential match
            for j in range(len(t)):                
                if s[i] == t[j]:
                    # When match is found, remove everything from match string up to and including the match
                    t = t[j+1:]
                    found = True
                    break 
                    
           # If any letter is not found in a pass, return False
            if found == False:
                return False
        # If all letters have been found, we will retun True
        return True
                    