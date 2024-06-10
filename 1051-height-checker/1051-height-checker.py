class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = [i for i in range(len(heights)) if heights[i] != expected[i]]
        return len(count)
        