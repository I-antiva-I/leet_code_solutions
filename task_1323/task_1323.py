# LeetCode #1323 | Maximum 69 Number | [EASY]

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        six_position = -1
        counter = 0
        temp = num

        while (temp != 0):
            if (temp % 10 == 6):
                six_position = counter
            temp = temp // 10
            counter += 1

        return num + 3*(10**six_position) if (six_position != -1) else num