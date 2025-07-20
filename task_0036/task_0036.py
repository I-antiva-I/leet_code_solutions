# LeetCode #0036 | Valid Sudoku | [MEDIUM]
# [!] IMPORTANT (Sudoku)

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows =  [set() for _ in range(9)]
        cols =  [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue

                b = (i // 3 ) * 3 + (j // 3)

                if cell in rows[i]:
                    return False

                if cell in cols[j]:
                    return False

                if cell in boxes[b]:
                    return False

                rows[i].add(cell)
                cols[j].add(cell)
                boxes[b].add(cell)

        return True