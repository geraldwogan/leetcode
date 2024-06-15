class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        x = {}
        
        for val in arr:
            x[val] = arr.count(val)
                    
        for k, val in enumerate(x):
            if list(x.values()).count(x[val]) >  1:
                return False
            
        return True 
