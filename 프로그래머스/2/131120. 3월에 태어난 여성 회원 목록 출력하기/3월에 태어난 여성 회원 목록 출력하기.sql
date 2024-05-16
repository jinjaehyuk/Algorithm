-- 코드를 입력하세요
SELECT member_id, member_name, gender, DATE_FORMAT(date_of_birth,"%Y-%m-%d") as date_of_birth
from MEMBER_PROFILE
where gender ='W'
and date_of_birth like '%-03-%'
and tlNo is not null
order by member_id