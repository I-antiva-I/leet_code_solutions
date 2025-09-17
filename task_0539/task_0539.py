# LeetCode #0539 | Minimum Time Difference | [MEDIUM]

class Solution(object):
    def timeDifference(self, time_a, time_b):
        delta = min(abs(time_a - time_b), 24*60 - abs(time_a - time_b))
        return delta

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        
        day_points = [-1]*24*60
        
        for tp in timePoints:
            h = int(tp[:2])
            m = int(tp[3:])
            day_points[h*60 + m] += 1
            if day_points[h*60 + m] > 0:
                return 0

        pivot_dp = int(timePoints[0][:2])*60+int(timePoints[0][3:])
        last_good_dp_cw = pivot_dp
        last_good_dp_ccw = pivot_dp

        for i in range(1, 24*60+1):
            # CW
            if day_points[(pivot_dp+i)%(24*60)] != -1:
                delta = self.timeDifference(last_good_dp_cw, (pivot_dp+i)%(24*60))
                if (delta < day_points[last_good_dp_cw]) or (day_points[last_good_dp_cw] == 0):
                    day_points[last_good_dp_cw] = delta
                last_good_dp_cw = (pivot_dp+i)%(24*60)
            # CCW
            if day_points[(pivot_dp-i)%(24*60)] != -1:
                delta = self.timeDifference(last_good_dp_ccw, (pivot_dp-i)%(24*60))
                if (delta < day_points[last_good_dp_ccw]) or (day_points[last_good_dp_ccw] == 0):
                    day_points[last_good_dp_ccw] = delta
                last_good_dp_ccw = (pivot_dp-i)%(24*60)
        
        min_delta = 24*60
        for dp in day_points:
            if (dp != -1) and (dp < min_delta):
                min_delta = dp

        return min_delta