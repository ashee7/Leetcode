# Write your MySQL query statement below
select a.student_id, a.student_name, b.subject_name , count(c.subject_name) as attended_exams
    from Students a cross join Subjects b 
        left join Examinations c on 
            b.subject_name = c.subject_name
            and a.student_id = c.student_id
    group by student_id,subject_name
    order by student_id,subject_name 