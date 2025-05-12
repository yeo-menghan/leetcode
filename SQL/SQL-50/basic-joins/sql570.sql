-- 570. Managers with at Least 5 Direct Reports
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50
SELECT
    e1.name
FROM
    Employee e1
JOIN
    Employee e2 ON e1.id = e2.managerId
GROUP BY
    e1.id
HAVING
    COUNT(*) >= 5;
