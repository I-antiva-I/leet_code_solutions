# LeetCode #0177 | Nth Highest Salary | [MEDIUM]

/*
(?) DECLARE and SET

By using the DECLARE statement, 
you can create variables with specific data types, 
which can then be assigned values 
using the SET or SELECT commands.

- geeksforgeeks
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE TrueOffset INT;
    SET TrueOffset = N-1;
    RETURN 
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET TrueOffset
    );
END

