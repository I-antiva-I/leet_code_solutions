# LeetCode #0383 | Ransom Note | [EASY] |

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        if (len(magazine) < len(ransomNote)):
            return False

        chars = [ [0,0] for _ in range(26) ]

        for char in ransomNote:
            chars[ord(char)-97][0] += 1
        
        for char in magazine:
            chars[ord(char)-97][1] += 1
    
        for char in chars:
            if (char[0] > char[1]):
                return False
        
        return True