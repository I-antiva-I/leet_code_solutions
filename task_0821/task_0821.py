# LeetCode #0821 | Shortest Distance to a Character | [EASY]

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """

        n = len(s)
        char_distances = [0]*n

        dist = n
        for i in range(n):
            if (s[i] == c):
                dist = i
            char_distances[i] = abs(dist - i)
        
        dist = n*2
        for i in range(n-1,-1,-1):
            if (s[i] == c):
                dist = i
            char_distances[i] = min(dist - i, char_distances[i])
     
        return char_distances