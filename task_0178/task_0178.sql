# LeetCode #0178 | Rank Scores | [MEDIUM]

/*
(?) RANK() 

The RANK() functions assigns the same rank to rows with duplicate values,
but introduces gaps in the ranking sequence for subsequent rows.

(?) DENSE_RANK()

Similar to RANK(), but does not leave gaps in the ranking sequence
for rows with the same value. If two rows are ranked 1st,
the next row will be ranked 2nd (not 3rd).

(?) ROW_NUMBER()

Fuction always assigns a unique sequential number to each row, 
without any gaps or handling of duplicates.

- geeksforgeeks
*/

SELECT 
    score, 
    DENSE_RANK() OVER 
        (ORDER BY score DESC) AS "rank"
FROM Scores;

/*
# (?) Alternative solution

SELECT S1.score, 
    (
    SELECT (COUNT(DISTINCT S2.score)) 
    FROM Scores AS S2
    WHERE S2.score >= S1.score
    ) AS "rank"
FROM Scores AS S1
ORDER BY score DESC
*/
