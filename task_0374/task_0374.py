# LeetCode #0374 | Guess Number Higher or Lower | [EASY]
# [!] IMPORTANT (Binary Search)

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        left_edge = 1
        right_edge = n

        while(left_edge <= right_edge):
            pivot = left_edge + (right_edge - left_edge) // 2  # Overflow safe.
            result = guess(pivot)

            if result > 0:
                left_edge = pivot + 1
            elif result < 0:
                right_edge = pivot - 1
            else:
                return pivot