# LeetCode #1742 | Maximum Number of Balls in a Box | [EASY]

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """

        boxes = {}
        max_balls = -1

        for number in range(lowLimit, highLimit+1):
            digit_sum = 0
            while (number > 0):
                digit_sum += number % 10
                number = number // 10

            boxes[digit_sum] = boxes.get(digit_sum, 0) + 1
            max_balls = max(max_balls, boxes[digit_sum])
        
        return max_balls