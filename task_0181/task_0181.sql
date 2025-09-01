# LeetCode #0181 | Employees Earning More Than Their Managers | [EASY]

SELECT E.name AS "Employee" FROM Employee AS E
JOIN Employee AS M
    ON E.managerId = M.id
WHERE E.salary > M.salary 