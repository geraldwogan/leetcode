class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Traversing list to find pivots
        for i, val in enumerate(nums):
            
            print(f'start {i}')
            # print(nums)
            # print(nums[i+1:])
            # print(nums[:i+1])
            
            leftsum=sum(nums[:i])
            rightsum = sum(nums[i+1:])
            
            # print(f'{nums[:i+1]} -> {leftsum}')
            # print(f'{nums[i+1:]} -> {rightsum}')
            if leftsum==rightsum:
                # print('woo!')
                return i
            
        return -1
        