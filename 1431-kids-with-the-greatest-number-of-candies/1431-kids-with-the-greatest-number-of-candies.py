class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        most = max(candies)
        results = []

        for i in candies:
            if i + extraCandies >= most:
                results.append(True)
            else:
                results.append(False) 

        return results
            