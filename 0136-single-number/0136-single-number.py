class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # only = []
        
        for val in nums:
            if nums.count(val) != 2:
                return val
                