-- 584. Find Customer Referee
-- https://leetcode.com/problems/find-customer-referee/description/?envType=study-plan-v2&envId=top-sql-50

SELECT
    name
FROM
    Customer
WHERE
    referee_id <> 2 OR referee_id IS null

/*
- In SQL, NULL means "unknown" or "no value".
- Any comparison with NULL (like <> 2) results in UNKNOWN, which is not TRUE.
*/


SELECT
    name
FROM
    Customer
WHERE
    COALESCE(referee_id, -1) <> 2

/*
Replace NULL with safe value and compare
BUT Can be slower because COALESCE applies a function on each row, potentially preventing index usage unless the index is on an expression matching COALESCE.
*/
