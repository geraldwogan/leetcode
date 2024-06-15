class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        alt = []
        alt.append(0)
        
        for i, val in enumerate(gain):
            alt.append(alt[i]+val)
            
        
        return max(alt)