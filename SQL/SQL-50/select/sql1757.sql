-- 1757. Recyclable and Low Fat Products
-- https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50
SELECT
    product_id
FROM
    Products
WHERE
    low_fats='Y' AND recyclable='Y'
