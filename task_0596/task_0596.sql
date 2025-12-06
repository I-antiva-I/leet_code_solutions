# LeetCode #0596 | Classes With at Least 5 Students | [EASY]

SELECT class FROM Courses
GROUP BY class
HAVING COUNT(student) > 4
