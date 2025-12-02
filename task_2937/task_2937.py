# LeetCode #2937 | Make Three Strings Equal | [EASY]

class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        
        min_len = min(len(s1), len(s2), len(s3)) 
        different_at = -1

        for i in range(min_len):
            if ((s1[i] != s2[i]) or (s1[i] != s3[i]) or (s2[i] != s3[i])):
                different_at = i
                break

        if (different_at == 0):
            return -1
        
        elif (different_at == -1):
            return (len(s1) - min_len) + (len(s2) - min_len) + (len(s3) - min_len) 
        
        else:
            return (min_len - different_at)*3 + (len(s1) - min_len) + (len(s2) - min_len) + (len(s3) - min_len) 

        
