# LeetCode #3265 | Count Almost Equal Pairs I | [MEDIUM] |
# [!] CAN BE IMPROVED 

class Solution(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        pairs = 0
        
        def breakDown(value):
            digits = []

            while(True):
                digits.append(value % 10)
                value = value // 10
                if (value == 0):
                    break

            return digits

        def checkDigits(d1, d2):
            bad_pairs = []

            for i in range(len(d1)):
                if (d1[i] != d2[i]):
                    bad_pairs.append([d1[i], d2[i]])

            if (len(bad_pairs) == 0):
                return True
            elif (len(bad_pairs) != 2):
                return False
            else:
                return ((bad_pairs[0][0] == bad_pairs[1][1]) and (bad_pairs[0][1] == bad_pairs[1][0]))

        for i in range(len(nums)):
            i_digits = breakDown(nums[i])

            for j in range(i+1, len(nums)):
                j_digits = breakDown(nums[j])

                delta = len(i_digits) - len(j_digits)

                if (delta == 0):
                    if (checkDigits(i_digits, j_digits)):
                        pairs += 1

                elif (delta > 0):
                    j_digits_with_leading_zeros = breakDown(nums[j])
                    leading_zeros = [0]*delta
                    j_digits_with_leading_zeros.extend(leading_zeros)

                    if (checkDigits(i_digits, j_digits_with_leading_zeros)):
                        pairs += 1
                        
                elif (delta < 0):
                    i_digits_with_leading_zeros = breakDown(nums[i])
                    leading_zeros = [0]*-delta
                    i_digits_with_leading_zeros.extend(leading_zeros)

                    if (checkDigits(i_digits_with_leading_zeros, j_digits)):
                        pairs += 1

        return pairs