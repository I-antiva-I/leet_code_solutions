# LeetCode #0867 | Transpose Matrix | [EASY]

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n = len(matrix)
        m = len(matrix[0])
        transposed = [[0 for _ in range(n)] for _  in range(m)]

        for i in range(n):
            for j in range(m):
                transposed[j][i] = matrix[i][j]
        
        return transposed