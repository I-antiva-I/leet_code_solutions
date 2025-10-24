# LeetCode #0345 | Reverse Vowels of a String | [EASY] |

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        s_as_list = list(s)
        vowels = [ 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' ]

        left = 0
        right = len(s)-1

        while (left < right):
            if (s_as_list[left] in vowels):
                while (s_as_list[right] not in vowels):
                    right -= 1
                s_as_list[left], s_as_list[right] = s_as_list[right], s_as_list[left]
                left += 1
                right -= 1
            else:
                left += 1
        
        return "".join(s_as_list)