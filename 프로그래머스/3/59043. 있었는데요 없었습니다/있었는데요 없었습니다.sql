-- 코드를 입력하세요
SELECT b.animal_id, b.name
from animal_ins a , animal_outs b 
where a.animal_id = b.animal_id
and a.datetime > b.datetime
order by a.datetime