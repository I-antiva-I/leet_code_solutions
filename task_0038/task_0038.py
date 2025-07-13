# LeetCode #0038 | Count and Say | [MEDIUM]

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = "1"
        for i in range(n-1):
            string = self.compressString(string)
        return string


    def compressString(self, chars):
        compressed = ""
        last = chars[0]
        repeats = 1
        for c in chars[1:]:
            if last == c:
                repeats += 1
            else:
                compressed += str(repeats) + last
                repeats = 1
                last = c
        compressed += str(repeats) + last
        return compressed

