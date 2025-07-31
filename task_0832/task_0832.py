# LeetCode #0832 | Flipping an Image | [EASY]

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """

        # [1,1,0]     [0,1,1]     [1,0,0]
        # [1,0,1] >>> [1,0,1] >>> [0,1,0]
        # [0,0,0]     [0,0,0]     [1,1,1]

        n = len(image)
        inverted = []

        for i in range(n):
            inverted.append([])
            for j in range(n):
                inverted[i].append(abs(image[i][n-j-1]-1))

        return inverted

