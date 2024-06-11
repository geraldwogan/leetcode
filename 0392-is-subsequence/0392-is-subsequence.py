class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
#         # Solution 1 - that I came up with on my own
#         # Loop over each letter that needs to be found
#         for i in range(len(s)):
#             found = False
#             # Loop over each letter that is a potential match
#             for j in range(len(t)):                
#                 if s[i] == t[j]:
#                     # When match is found, remove everything from match string up to and including the match
#                     t = t[j+1:]
#                     found = True
#                     break 
                    
#            # If any letter is not found in a pass, return False
#             if found == False:
#                 return False
#         # If all letters have been found, we will retun True
#         return True
                    
        # Solution 2 - attempting to follow the solution guide on leetcode
        left_pointer, right_pointer = 0 , 0
        print(left_pointer)
        print(right_pointer)
        
        while left_pointer < len(s) and right_pointer < len(t):
            if s[left_pointer] == t[right_pointer]:
                # Match found, iterate both
                left_pointer += 1
                right_pointer += 1
            else:
                # No match, try next letter in t
                right_pointer +=1
        if left_pointer == len(s):
            return True
        else:
            return False
            
            