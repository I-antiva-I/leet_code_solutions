# LeetCode #2138 | Divide a String Into Groups of Size k | [EASY]

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        
        groups = []
        g = -1

        for i in range(len(s)):
            if (i % k == 0):
                groups.append("")
                g += 1
            groups[g] += s[i]

        if (len(s) % k != 0):
            groups[g] += fill*(k-(len(s)%k))

        return groups