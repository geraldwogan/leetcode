class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # base case:
        if len(nums) == 0:
            return 0
        print(nums)
        # Reverse bubble sort?
        for i in range(len(nums)-1, -1, -1):
            # nums.remove()
            print(i)
            # HMmm... bubble sort
            swapped = False
            for j in range(len(nums)-i-2, -1, -1):
                print(f'(j) {nums[j]} vs. {nums[j+1]}')
                if nums[j] == val:
                    print('swapa')
                    # nums[j], nums[j+1] = nums[j+1], nums[j]
                    nums.remove(nums[j])
                
            if swapped == True:
                break
        if val in nums:
            nums.remove(val)
        # for
        # nums = nums.split(val)[0]
        return  len(nums)
        # print(nums)
        # # for i in range(len(nums )-1, -1, -1):
        # keeps = []
        # for i in range(len(nums)):
        #     print(i)
        #     if nums[i] != val:
        #         keeps.append(i)
        #         print(f'remove {i}')
        #         nums.remove(nums[i])
        # nums = nums[[1,3]]