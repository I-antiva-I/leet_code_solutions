# LeetCode #1790 | Check if One String Swap Can Make Strings Equal | [EASY] |

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        bad_pairs = []

        for i in range(len(s1)):
            if (s1[i] != s2[i]):
                bad_pairs.append([s1[i], s2[i]])

        if (len(bad_pairs) == 0):
            return True
        elif (len(bad_pairs) != 2):
            return False
        else:
            return ((bad_pairs[0][0] == bad_pairs[1][1]) and (bad_pairs[0][1] == bad_pairs[1][0]))
