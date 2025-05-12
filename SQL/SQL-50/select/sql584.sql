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
