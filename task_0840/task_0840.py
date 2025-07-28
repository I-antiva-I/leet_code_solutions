# LeetCode #0840 | Magic Squares In Grid | [MEDIUM]

class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
		
        nr = len(grid)
        nc = len(grid[0])
        ms = 0

        for i in range(nr-2):
            for j in range(nc-2):

                if grid[i+1][j+1] != 5:
                    continue
                
                values = {  grid[i  ][j  ],grid[i  ][j+1],grid[i  ][j+2],
                            grid[i+1][j  ],grid[i+1][j+1],grid[i+1][j+2],
                            grid[i+2][j  ],grid[i+2][j+1],grid[i+2][j+2]}

                if values != {1,2,3,4,5,6,7,8,9}:
                    continue

                r1 = grid[i  ][j  ]+grid[i  ][j+1]+grid[i  ][j+2]
                r2 = grid[i+1][j  ]+grid[i+1][j+1]+grid[i+1][j+2]
                r3 = grid[i+2][j  ]+grid[i+2][j+1]+grid[i+2][j+2]
                d1 = grid[i  ][j  ]+grid[i+1][j+1]+grid[i+2][j+2]
                d2 = grid[i+2][j  ]+grid[i+1][j+1]+grid[i  ][j+2]
                c1 = grid[i  ][j  ]+grid[i+1][j  ]+grid[i+2][j  ]
                c2 = grid[i  ][j+1]+grid[i+1][j+1]+grid[i+2][j+1]
                c3 = grid[i  ][j+2]+grid[i+1][j+2]+grid[i+2][j+2]

                if len({r1, r2, r3, c1, c2, c3, d1, d2}) == 1:
                    ms += 1
        
        return ms
                