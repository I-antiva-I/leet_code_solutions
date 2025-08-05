# LeetCode #0067 | Add Binary | [EASY]

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        result = ""
        remember = 0
        index = 1

        while (index <= len(a)) or (index <= len(b)):

            a_val = 1 if index <= len(a) and a[-index] == "1" else 0
            b_val = 1 if index <= len(b) and b[-index] == "1" else 0

            result += "1" if (a_val+b_val+remember) % 2 else "0"
            remember = (a_val+b_val+remember) // 2

            index +=1

        if remember:
            result += "1"

        return result[::-1]
