# LeetCode #0414 | Third Maximum Number | [EASY] |

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_1 = None
        max_2 = None
        max_3 = None

        for n in nums:
            
            if (n > max_1) or (max_1 is None):
                max_3 = max_2
                max_2 = max_1
                max_1 = n

            elif ((n > max_2) or (max_2 is None)) and (n != max_1):
                max_3 = max_2
                max_2 = n

            elif ((n > max_3) or (max_3 is None)) and ((n != max_2) and (n != max_1)):
                max_3 = n

        return max_3 if (max_3 is not None) else max_1