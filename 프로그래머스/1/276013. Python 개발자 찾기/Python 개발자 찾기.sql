-- 코드를 작성해주세요
select  id, email, first_name, last_name
from DEVELOPER_INFOS
where skill_1 like 'python' 
or skill_2 like 'python' 
or skill_3 like 'python' 
order by id 