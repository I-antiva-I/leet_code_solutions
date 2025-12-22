# LeetCode #1741 | Find Total Time Spent by Each Employee | [EASY]

SELECT event_day AS "day", emp_id, SUM(out_time-in_time) AS "total_time" FROM Employees
GROUP BY event_day, emp_id
ORDER BY event_day ASC, emp_id ASC