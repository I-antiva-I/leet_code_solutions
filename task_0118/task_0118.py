# LeetCode #0118 | Pascal's Triangle | [EASY]

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        final = []

        for i in range(numRows):
            mid = [1] * (i+1)

            for j in range(i-1):
                mid[j+1] = final[i-1][j] + final[i-1][j+1]
            final.append(mid)

        return final