# LeetCode #1431 | Kids With the Greatest Number of Candies | [EASY]

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        max_candies = max(candies)
        result = []
        for c in candies:
            result.append((c+extraCandies >= max_candies))
        return result