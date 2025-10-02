# LeetCode #0925 | Long Pressed Name | [EASY] |

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
    
        condensed_name = []
        condensed_typed = []
        
        condensed_size = 0
        previous_char = "?"
        for char in name:
            if (char == previous_char):
                condensed_name[condensed_size-1][1] += 1
            else:
                previous_char = char
                condensed_name.append([char, 1])
                condensed_size += 1
        
        condensed_size = 0
        previous_char = "?"
        for char in typed:
            if (char == previous_char):
                condensed_typed[condensed_size-1][1] += 1
            else:
                previous_char = char
                condensed_typed.append([char, 1])
                condensed_size += 1

        if (len(condensed_name) != len(condensed_typed)):
            return False

        for i in range(condensed_size):
            if ((condensed_name[i][0] != condensed_typed[i][0]) or
                (condensed_name[i][1] > condensed_typed[i][1])):
                return False

        return True