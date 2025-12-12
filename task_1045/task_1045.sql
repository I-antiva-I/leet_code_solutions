# LeetCode #1045 | Customers Who Bought All Products | [MEDIUM]

SELECT DISTINCT C.customer_id FROM Customer AS C
GROUP BY C.customer_id 
HAVING COUNT(DISTINCT C.product_key) =
(
    SELECT COUNT(P.product_key) FROM Product AS P 
)
ORDER BY C.customer_id