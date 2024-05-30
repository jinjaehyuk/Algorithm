-- 코드를 작성해주세요
select he.dept_id, hd.DEPT_NAME_EN, round(avg(sal)) as avg_sal
from HR_DEPARTMENT hd, HR_EMPLOYEES he
where hd.dept_id = he.dept_id
group by he.dept_id, hd.DEPT_NAME_EN
order by avg(sal) desc