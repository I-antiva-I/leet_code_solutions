# LeetCode #0176 | Second Highest Salary | [MEDIUM]

/*
(?) MIN and MAX

The MIN() function returns 
the smallest value of the selected column.

The MAX() function returns 
the largest value of the selected column.

- w3schools
*/

SELECT MAX(salary)
AS SecondHighestSalary
FROM Employee
WHERE salary <
    (
        SELECT MAX(salary)
        FROM Employee
    );