class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        dupes = [x for x in nums1 if x in nums2 ]
        print(dupes)
        
        n1 = [z for z in nums1 if z not in dupes]
        n2 = [y for y in nums2 if y not in dupes]
        
        answers = [set(n1), set(n2)]
        
        return answers