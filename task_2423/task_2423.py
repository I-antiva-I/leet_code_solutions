# LeetCode #2423 | Remove Letter To Equalize Frequency | [EASY] |

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        freqs = [0 for _ in range(26)]

        for char in word:
            freqs[ord(char)-97] += 1
        
        # Key --> frequency; Value --> occurences of that frequency
        uniq_freqs = {}

        for f in freqs:
            if (f != 0):
                uniq_freqs[f] = uniq_freqs.get(f, 0) + 1

        if (len(uniq_freqs) > 2):
            return False
        elif (len(uniq_freqs) == 1): 
            return (uniq_freqs.items()[0][0] == 1) or (uniq_freqs.items()[0][1] == 1)
        else:
            largest_freq = max(uniq_freqs.keys()[0], uniq_freqs.keys()[1])
            smallest_freq = min(uniq_freqs.keys()[0], uniq_freqs.keys()[1])

            if (smallest_freq == 1) and (uniq_freqs[smallest_freq] == 1):
                return True

            freq_diff = largest_freq - smallest_freq
            has_largest_freq_occured_once = (uniq_freqs[largest_freq] == 1)

            if (freq_diff == 1) and (has_largest_freq_occured_once):
                return True
            
            return False