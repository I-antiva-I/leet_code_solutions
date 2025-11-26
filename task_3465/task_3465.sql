# LeetCode #3465 | Find Products with Valid Serial Numbers | [EASY]

SELECT * FROM PRODUCTS
WHERE REGEXP_LIKE(description,'\\bSN[0-9]{4}-[0-9]{4}\\b', 'c')
ORDER BY product_id
