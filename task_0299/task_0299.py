# LeetCode #0299 | Bulls and Cows | [MEDIUM] |

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        right_place_right_char = 0
        wrong_place_right_char = 0
        chars = {}

        for i in range(len(secret)):
            if (secret[i] == guess[i]):
                right_place_right_char += 1
            else:
                chars.setdefault(secret[i], [0,0])[0] += 1
                chars.setdefault(guess[i],  [0,0])[1] += 1

        for v in chars.values():
            wrong_place_right_char += min(v)

        return str(right_place_right_char)+'A'+str(wrong_place_right_char)+'B'
