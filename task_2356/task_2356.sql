# LeetCode #2356 | Number of Unique Subjects Taught by Each Teacher | [EASY]

/*

(?) COUNT(DISTINCT column_name)
When combined, COUNT and DISTINCT can be 
used to count the number of unique values
in a column or a set of columns.

*/

SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt FROM Teacher
GROUP BY teacher_id
