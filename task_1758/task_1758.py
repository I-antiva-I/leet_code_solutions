# LeetCode #1758 | Minimum Changes To Make Alternating Binary String | [EASY]

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
 
        changes_zero_one = [0, 0]
        expect_zero_one = ["0", "1"]

        for i in range(len(s)):
            changes_zero_one[0] += 0 if (s[i] == expect_zero_one[(i+0)%2]) else 1
            changes_zero_one[1] += 0 if (s[i] == expect_zero_one[(i+1)%2]) else 1

        return min(changes_zero_one)
