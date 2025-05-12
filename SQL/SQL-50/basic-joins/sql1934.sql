-- 1934. Confirmation Rate
-- https://leetcode.com/problems/confirmation-rate/description/?envType=study-plan-v2&envId=top-sql-50
SELECT
    u1.user_id,
    ROUND(
        COALESCE(
            SUM(CASE WHEN u2.action = 'confirmed' THEN 1 ELSE 0 END) * 1.0 / NULLIF(COUNT(u2.action), 0),
            0
        ), 2
    ) as confirmation_rate
FROM
    Signups u1
LEFT JOIN
    Confirmations u2 ON u1.user_id = u2.user_id
GROUP BY
    u1.user_id
