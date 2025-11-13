# LeetCode #3386 | Button with Longest Push Time | [EASY]

class Solution(object):
    def buttonWithLongestTime(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        
        max_time = events[0][1]
        max_index = events[0][0]

        for i in range(1, len(events)):
            time = events[i][1] - events[i-1][1]

            if (time > max_time):
                max_time = time
                max_index = events[i][0]

            elif (time == max_time):
                max_index = min(max_index, events[i][0])
        
        return max_index