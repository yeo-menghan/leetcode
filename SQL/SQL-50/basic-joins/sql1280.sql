-- 1280. Students and Examinations
-- https://leetcode.com/problems/students-and-examinations/description/?envType=study-plan-v2&envId=top-sql-50

SELECT
    stu.student_id,
    stu.student_name,
    subj.subject_name,
    COUNT(exam.student_id) AS attended_exams
FROM
    Students stu
CROSS JOIN
    Subjects subj
LEFT JOIN
    Examinations exam
    ON stu.student_id = exam.student_id
    AND subj.subject_name = exam.subject_name
GROUP BY
    stu.student_id,
    subj.subject_name
ORDER BY
    stu.student_id,
    subj.subject_name;

/*
- CROSS JOIN produces the Cartesian product — every student combined with every subject.
    - count how many times each student attended each subject, including subjects where the student has zero attendance.
- The GROUP BY clause is necessary because you want to aggregate (count exams attended)
    -  count per unique combination of student and subject.
*/
