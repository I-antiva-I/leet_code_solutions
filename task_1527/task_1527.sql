# LeetCode #1527 | Patients With a Condition | [EASY]

/*

(?) LIKE

The LIKE operator is used in a WHERE clause to search for a specified pattern in a column.

There are two wildcards often used in conjunction with the LIKE operator:
    > The percent sign % represents zero, one, or multiple characters;
    > The underscore sign _ represents one, single character;

*/

SELECT * FROM Patients
WHERE conditions LIKE "% DIAB1%" OR conditions LIKE "DIAB1%" 