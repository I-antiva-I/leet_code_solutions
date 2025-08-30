# LeetCode #0180 | Consecutive Numbers | [MEDIUM]

/*
(?) LAG(column)

The LAG() function is used to get value from the row,
which precedes the current row.

(?) LEAD(column)

The LEAD() function is used to get value from a row,
which succeeds the current row.

- geeksforgeeks
*/

SELECT DISTINCT num AS "ConsecutiveNums" 
FROM 
(
    SELECT num, 
           LAG(num) OVER (ORDER BY id) AS prev,
           LEAD(num) OVER (ORDER BY id) AS next
    FROM Logs
) AS LogsX
WHERE  prev = num AND next = num

/*
# (?) Alternative solution

# (?) FROM TableOne AS T1, TableTwo AS T2, ...,  TableN AS TN will produce a CROSS JOIN.

SELECT DISTINCT L1.num AS "ConsecutiveNums"
FROM Logs AS L1, Logs AS L2, Logs AS L3
WHERE
    (L1.id - 1 = L2.id AND L3.id + 1 = L2.id)
    AND 
    (L1.num = L2.num AND L3.num = L2.num);

*/
