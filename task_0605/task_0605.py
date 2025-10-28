# LeetCode #0605 | Can Place Flowers | [EASY] |

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        s = len(flowerbed)

        for i in range(s):
            if (n == 0):
                break
            
            prev_plot = -1 if (i-1 == -1) else flowerbed[i-1]
            curr_plot = flowerbed[i]
            next_plot = -1 if (i+1 == s) else flowerbed[i+1]
            
            if ((prev_plot != 1) and (curr_plot != 1) and (next_plot != 1)):
                flowerbed[i] = 1
                n -= 1

        return (n == 0)