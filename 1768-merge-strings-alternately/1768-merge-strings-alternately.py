class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ''
        short = min([len(word1),len(word2)])
        long = max(word1,word2, key=len)
        
        for i in range(short):
            word += word1[i] + word2[i]
            
        word += long[short:]  
        
        return word
    

        