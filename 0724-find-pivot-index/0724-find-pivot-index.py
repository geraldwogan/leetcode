class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Traversing list to find pivots
        for i, val in enumerate(nums):
            
            # print(f'start {i}')
            # print(f'{nums[:i+1]} -> {leftsum}')
            # print(f'{nums[i+1:]} -> {rightsum}')
            
            leftsum = sum(nums[:i])
            rightsum = sum(nums[i+1:])
            
            if leftsum==rightsum:
                return i
            
        return -1
        