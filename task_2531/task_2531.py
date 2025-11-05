# LeetCode #2531 | Make Number of Distinct Characters Equal | [MEDIUM] |

class Solution(object):
    def isItPossible(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        chars = [ [0,0] for _ in range(26) ]
        uniques = [0, 0]
   
        for char in word1:
            chars[ord(char)-97][0] += 1

        for char in word2:
            chars[ord(char)-97][1] += 1

        for i in range(26):
            for j in range(2):
                if chars[i][j] != 0:
                    uniques[j] += 1

        if (abs(uniques[0] - uniques[1]) > 2):
            return False
        
        uniques_delta = [0, 0]

        for i in range(26):
            if (chars[i][0] == 0):
                    continue
                
            for j in range(26):
                if (chars[j][1] == 0):
                        continue

                # Move I ----> J
                uniques_delta[0] = -1 if (chars[i][0] == 1) else 0
                uniques_delta[1] = 0 if (chars[i][1] > 0) else +1
                
                # Move J ----> I
                uniques_delta[1] += -1 if (chars[j][1] + int(i == j) == 1) else 0
                uniques_delta[0] += 0 if (chars[j][0]  - int(i == j) > 0) else +1

                if (abs((uniques[0]+uniques_delta[0]) - (uniques[1]+uniques_delta[1])) == 0):
                    return True
                    
        return False