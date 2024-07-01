-- 코드를 입력하세요
SELECT YEAR(sales_date) year, MONTH(sales_date) as month, gender, COUNT(DISTINCT ui.USER_ID) USERS
from user_info ui, online_sale os
where ui.user_id = os.user_id
and gender is not null
group by YEAR,MONTH, gender
order by YEAR,MONTH,gender


