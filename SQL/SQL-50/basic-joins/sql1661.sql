-- 1661. Average Time of Process per Machine
-- https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50

SELECT
    st.machine_id,
    ROUND(AVG(et.timestamp-st.timestamp), 3) as processing_time
FROM
    Activity st
JOIN
    Activity et
    ON st.machine_id=et.machine_id
    AND st.process_id=et.process_id
    AND st.activity_type='start'
    AND et.activity_type='end'
GROUP BY st.machine_id
ORDER BY st.machine_id
