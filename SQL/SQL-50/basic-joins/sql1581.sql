-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/?envType=study-plan-v2&envId=top-sql-50

SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM
    Visits v
LEFT JOIN
    Transactions t ON v.visit_id = t.visit_id
WHERE
    t.visit_id IS NULL
GROUP BY
    v.customer_id

/*
- LEFT JOIN pairs each visit with any matching transaction.
- If there is no transaction for a visit, t.visit_id will be NULL.
- The WHERE t.visit_id IS NULL filters only visits without transactions.
- Then we count how many such visits each user made.
- GROUP BY customer_id aggregates visits per user.
*/
