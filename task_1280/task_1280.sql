# LeetCode #1280 | Students and Examinations | [EASY]

/*

(?) CROSS JOIN 
The CROSS JOIN keyword returns all records from both tables (table1 and table2).

T1   |   T2
A    |   X
B    |   Y

CROSS JOIN
A X
A Y
B X
B Y

*/


SELECT S.student_id, S.student_name, L.subject_name, count(E.subject_name) AS "attended_exams" FROM Students AS S
CROSS JOIN Subjects AS L 
LEFT JOIN Examinations AS E
    ON S.student_id = E.student_id AND L.subject_name = E.subject_name 
GROUP BY S.student_id, L.subject_name 
ORDER BY S.student_id ASC, L.subject_name ASC
