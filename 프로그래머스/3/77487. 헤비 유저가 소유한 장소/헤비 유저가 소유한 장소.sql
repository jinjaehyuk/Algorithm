-- 코드를 입력하세요
select *
from places
where host_id in (
SELECT host_id
from PLACES
group by host_id
having count(*) > 1
) 
order by id 