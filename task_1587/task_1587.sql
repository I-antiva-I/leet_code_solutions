# LeetCode #1587 | Bank Account Summary II | [EASY]

SELECT U.name, SUM(T.amount) AS "balance" FROM Users AS U
JOIN Transactions AS T ON T.account = U.account
GROUP BY U.account 
HAVING SUM(T.amount) > 10000
ORDER BY U.name DESC
