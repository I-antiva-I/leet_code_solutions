# LeetCode #0054 | Spiral Matrix | [MEDIUM]

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        spiral = []
        count = 0
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        row_dir = 0
        col_dir = 1
        r = 0
        c = 0
        coils = 0
    
        while (count < n_cols*n_rows):
            spiral.append(matrix[r][c])
            count += 1
            r += row_dir
            c += col_dir

            if ((r == n_rows - coils and row_dir == 1) or
                (c == n_cols - coils and col_dir == 1) or
                (r == -1 + coils and row_dir == -1) or
                (c == -1 + coils and col_dir == -1) ):

                    if col_dir == 1:
                        row_dir = 1
                        col_dir = 0
                        c -= 1
                        r += 1
                    elif row_dir == 1:
                        row_dir = 0
                        col_dir = -1
                        r -= 1
                        c -= 1
                    elif col_dir == -1:
                        row_dir = -1
                        col_dir = 0
                        c += 1
                        r -= 1
                        coils += 1
                    else:
                        row_dir = 0
                        col_dir = 1
                        r += 1
                        c += 1
        
        return spiral