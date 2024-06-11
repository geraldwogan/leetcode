class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # base case:
        if len(nums) == 0:
            return 0

        for i in range(len(nums)-1, -1, -1):
            swapped = False
            for j in range(len(nums)-i-2, -1, -1):
                if nums[j] == val:
                    nums.remove(nums[j])
                
            if swapped == True:
                break
        if val in nums:
            nums.remove(val)

        return  len(nums)

        