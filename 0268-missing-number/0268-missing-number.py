class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        
        if (nums[0] != 0):
            return 0
        
        match = nums[0]
        
        for x in nums:
            if match != x:
                return match
            match += 1
            
        return nums[-1]+1
