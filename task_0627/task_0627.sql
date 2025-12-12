# LeetCode #0627 | Swap Sex of Employees | [EASY]

/*

(?) UPDATE
The UPDATE statement is used to modify the existing records in a table.

(?) CASE
The CASE expression goes through conditions and returns a value when the first condition is met (like an if-then-else statement). 
If no conditions are true, it returns the value in the ELSE clause.
If there is no ELSE part and no conditions are true, it returns NULL.

*/

UPDATE Salary
SET sex = 
CASE
    WHEN sex = 'm' THEN 'f'
    WHEN sex = 'f' THEN 'm'
END;