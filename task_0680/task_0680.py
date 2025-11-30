# LeetCode #0680 | Valid Palindrome II | [EASY]

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l = len(s)

        for i in range(l//2):
            if s[i] != s[l-1-i]:
                left_check = True
                right_check = True

                # Left
                for j in range(i,l//2):
                    if s[j+1] != s[l-1-j]: 
                        left_check = False
                        break
                
                # Right
                for j in range(i,l//2):
                    if s[j] != s[l-1-j-1]: 
                        right_check = False
                        break
                
                # Check
                if (left_check) or (right_check):
                    return True
                else:
                    return False

        return True