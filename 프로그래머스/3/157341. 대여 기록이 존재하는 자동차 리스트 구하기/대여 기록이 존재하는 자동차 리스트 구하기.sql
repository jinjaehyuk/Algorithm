-- 코드를 입력하세요
SELECT distinct crcc.car_id
from CAR_RENTAL_COMPANY_CAR crcc, CAR_RENTAL_COMPANY_RENTAL_HISTORY crcrh
where crcc.car_id = crcrh.car_id
and crcrh.start_date like '%-10-%'
and crcc.car_type ='세단'
order by crcc.car_id desc