# LeetCode #0602 | Friend Requests II: Who Has the Most Friends | [MEDIUM]

/*

(?) UNION - removes duplicate records.
(?) UNION ALL - includes all duplicates.

*/

SELECT id, SUM(num) AS num FROM
(
    SELECT requester_id AS id, COUNT(accepter_id) AS num FROM RequestAccepted
    GROUP BY requester_id 
    UNION ALL
    SELECT accepter_id AS id, COUNT(requester_id) AS num FROM RequestAccepted
    GROUP BY accepter_id 
) AS U
GROUP BY id
ORDER BY SUM(num) DESC
LIMIT 1
