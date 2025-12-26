# LeetCode #1484 | Group Sold Products By The Date | [EASY]

/*

(?) GROUP_CONCAT

The GROUP_CONCAT() function in MySQL is an aggregation function, which
combines data from multiple rows into a single string.
It is particularly useful for aggregating summaries,
such as combining related information into a single field.

*/

SELECT sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
FROM Activities 
GROUP BY sell_date
ORDER BY sell_date
