class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Map ints to str
        d = map(str, digits)
        # Make list into str, and then into int
        d = int(''.join(d))
        # Increment int by 1
        d += 1
        # Create list from int (needs to be str first)
        d = list(str(d))
        # Map list of str to list of ints
        d = map(int, d)
        
        # print(d)
        
        return d
