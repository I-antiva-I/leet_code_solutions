# LeetCode #0119 | Pascal's Triangle II | [EASY]

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        tria = [1] * (rowIndex+1)

        for i in range(rowIndex):
            for j in range(i, 0, -1):
                tria[j] += tria[j-1]
        
        return tria

        # (+) Alternative solution (formula):
        """
        tria = [1]
        for i in range(rowIndex):
            next_val = tria[-1] * (rowIndex - i) // (i + 1)
            tria.append(next_val)
        return tria
        """
