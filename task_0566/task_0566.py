# LeetCode #0566 | Reshape the Matrix | [EASY]

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        t = len(mat[0]) * len(mat)
        if (t // r == c) and (t % r == 0):
            new = [[0 for _ in range(c)] for _ in range(r)]
            x = 0

            for row in mat:
                for val in row:
                    new[x // c][x % c] = val
                    x += 1

            return new
        else:
            return mat