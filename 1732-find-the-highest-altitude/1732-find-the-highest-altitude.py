class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        alt = []
        alt.append(0)
        
        for i, val in enumerate(gain):
            alt.append(int(alt[i])+int(val))
            
        
        return max(alt)