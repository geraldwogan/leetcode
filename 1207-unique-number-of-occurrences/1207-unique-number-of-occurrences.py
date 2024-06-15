class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        x = {}
        
        for val in arr:
            x[val] = arr.count(val)
            
        print(x)
        
        for k, val in enumerate(x):
            print(k)
            print(val)
            print(x[val])
            # print(x.values().remove(x[val]))
            if list(x.values()).count(x[val]) >  1:
                return False
            
        return True 
