# LeetCode #0175 | Combine Two Tables | [EASY]

/*
(?) LEFT JOIN

The LEFT JOIN keyword returns all 
records from the left table (table1), 
and the matching records (if any) from 
the right table (table2).

- w3schools
*/

SELECT P.firstName, P.lastName, A.city, A.state
FROM Person AS P
LEFT JOIN Address AS A 
ON P.personId = A.personId;