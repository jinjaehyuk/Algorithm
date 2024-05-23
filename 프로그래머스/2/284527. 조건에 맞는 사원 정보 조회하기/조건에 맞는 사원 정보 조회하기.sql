-- 코드를 작성해주세요
select t.score, t.emp_no, emp_name, position,email
from HR_EMPLOYEES he, HR_DEPARTMENT hd, 
(select emp_no , sum(score) as score
from hr_grade
group by emp_no
order by score desc 
limit 1) t
where he.dept_id = hd.dept_id
and t.emp_no = he.emp_no



