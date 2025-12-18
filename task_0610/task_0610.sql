# LeetCode #0610 | Triangle Judgement | [EASY]

SELECT x, y, z, IF((x+y>z) AND (y+z>x) AND (z+x>y), "Yes", "No") AS triangle FROM Triangle
