# LeetCode #0184 | Department Highest Salary | [MEDIUM]

SELECT D.name AS "Department", E.name AS "Employee", E.salary AS "Salary" 
FROM Employee AS E
JOIN Department AS D ON D.id = E.departmentId 
JOIN
(
    SELECT 
        MAX(salary) AS "salary", departmentId 
    FROM Employee AS E 
    GROUP BY departmentId
) AS MaxSal
ON E.salary = MaxSal.salary AND E.departmentId = MaxSal.departmentId
ORDER BY E.departmentId