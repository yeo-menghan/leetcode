-- 1068. Product Sales Analysis I
-- https://leetcode.com/problems/product-sales-analysis-i/description/?envType=study-plan-v2&envId=top-sql-50
SELECT
    Product.product_name,
    Sales.year,
    Sales.price
FROM
    Sales
INNER JOIN Product ON Product.product_id=Sales.product_id
