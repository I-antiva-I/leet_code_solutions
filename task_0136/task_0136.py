# LeetCode #0136 | Single Number | [EASY]

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # XOR Rulues:
        # -----
        # Identity Rule         ->  A ^ 0 = A
        # Self-Inverse Rule     ->  A ^ A = 0
        # Commutative Property  ->  A ^ B = B ^ A
        # Associative Property  ->  A ^ (B ^ C) = (A ^ B) ^ C
        # -----

        xor = 0
        for num in nums:    
            xor = xor ^ num
        
        return xor