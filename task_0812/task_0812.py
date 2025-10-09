# LeetCode #0812 | Largest Triangle Area | [EASY]
# [!] IMPORTANT (Shoelace formula + Determinant)

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        
        max_area = 0
        n = len(points)

        for p1 in range(n):
            for p2 in range(p1+1,n):
                for p3 in range(p2+1,n):
                    x1,y1 = points[p1]
                    x2,y2 = points[p2]
                    x3,y3 = points[p3]

                    det1 = x1 * y2 - y1 * x2
                    det2 = x2 * y3 - y2 * x3
                    det3 = x3 * y1 - y3 * x1

                    area = abs(det1 + det2 + det3)

                    if (area > max_area):
                        max_area = area
        
        return max_area*0.5
