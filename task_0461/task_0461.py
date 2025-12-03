# LeetCode #0461 | Hamming Distance | [EASY]

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        diff = bin(x ^ y)[2:].count("1")
        return diff

        # Alternative solution:

        """
        bin_x = bin(x)[2:]      # Alternative method: f'{value:08b}'
        bin_y = bin(y)[2:]      # Alternative method: f'{value:08b}'

        n = max(len(bin_x), len(bin_y))
        bin_x = bin_x.rjust(n, "0")
        bin_y = bin_y.rjust(n, "0")

        diff = 0

        for i in range(n):
            if bin_x[i] != bin_y[i]:
                diff += 1

        return diff
        """
        