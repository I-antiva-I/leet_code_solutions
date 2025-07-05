# LeetCode #1051 | Height Checker | [EASY]

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        errors = 0
        for expected, real in zip(sorted(heights), heights):
            if expected != real:
                errors +=1

        return errors