# LeetCode #1890 | The Latest Login in 2020 | [EASY]

SELECT user_id, MAX(time_stamp) AS "last_stamp" FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id
