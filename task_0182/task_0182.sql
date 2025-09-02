# LeetCode #0182 | Duplicate Emails | [EASY]

/*
(?) GROUP BY
The GROUP BY statement groups rows, 
which have the same values into summary rows, 
for example "find the number of customers in each country".
The GROUP BY statement is often used with HAVING and AGGREGATE FUNCTIONS.

(?) HAVING
The HAVING clause was added to SQL,
because the WHERE keyword cannot be used with aggregate functions.

(?) AGGREGATE FUNCTIONS 
The most commonly used SQL aggregate functions are:
    > MIN() - returns the smallest value within the selected column
    > MAX() - returns the largest value within the selected column
    > COUNT() - returns the number of rows in a set
    > SUM() - returns the total sum of a numerical column
    > AVG() - returns the average value of a numerical column

- w3schools
*/

SELECT DISTINCT email AS "Email"
FROM Person
GROUP BY email
HAVING COUNT(email) > 1

/*
# (?) Alternative solution

SELECT DISTINCT P1.email AS "Email"
FROM Person AS P1
JOIN Person AS P2 
WHERE P2.id <> P1.id AND P1.email = P2.email
*/