# LeetCode #1407 | Top Travellers | [EASY]

/*
(?) COALESCE

The COALESCE function returns the first non-null value from a list of expressions.
If all values are null, it returns null. It’s commonly used to handle missing values or
combine multiple columns into one fallback output.
*/

SELECT U.Name, COALESCE(SUM(R.distance), 0) AS travelled_distance FROM Users AS U
LEFT JOIN Rides AS R
ON U.id = R.user_id
GROUP BY U.id  
ORDER BY SUM(R.distance) DESC, U.Name ASC
