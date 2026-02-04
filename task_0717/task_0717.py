# LeetCode #0717 | 1-bit and 2-bit Characters | [EASY]

class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        
        last_one_bit = False
        n = len(bits)
        i = 0
        
        while(i < n):
            if (bits[i] == 0):
                i += 1
                last_one_bit = True
            else:
                i += 2
                last_one_bit = False

        return last_one_bit
        