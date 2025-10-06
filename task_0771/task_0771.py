# LeetCode #0771 | Jewels and Stones | [EASY]

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        stones_that_are_also_jewels = 0

        for stone in stones:
            if stone in jewels:
                stones_that_are_also_jewels += 1

        return stones_that_are_also_jewels