-- 코드를 입력하세요
select date_format(sales_date,'%Y-%m-%d') as sales_date, product_id, IFNULL(USER_ID, NULL) AS USER_ID, sales_amount
from online_sale  
where sales_date like '2022-03%'
union
select date_format(sales_date,'%Y-%m-%d') as sales_date, product_id, NULL, sales_amount
from  offline_sale 
where sales_date like '2022-03%' 
order by sales_date,product_id, user_id

