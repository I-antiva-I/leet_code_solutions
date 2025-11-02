# LeetCode #2125 | Number of Laser Beams in a Bank | [MEDIUM] |

class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        
        prev_ones = bank[0].count("1")
        lasers = 0

        for row in bank[1:]:
            ones = row.count("1")
            if (ones == 0):
                continue
            else:
                lasers += ones*prev_ones
                prev_ones = ones
        
        return lasers
        