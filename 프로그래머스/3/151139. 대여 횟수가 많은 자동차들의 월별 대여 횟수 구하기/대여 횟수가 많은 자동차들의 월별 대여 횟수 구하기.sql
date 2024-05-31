-- 코드를 입력하세요
select month(start_date) as month, car_id, count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where car_id in (
SELECT car_id
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(start_date) between '08' and '10'
group by car_id 
having count(*) > 4
)
and month(start_date) between '08' and '10'
group by month ,car_id
order by month , car_id desc