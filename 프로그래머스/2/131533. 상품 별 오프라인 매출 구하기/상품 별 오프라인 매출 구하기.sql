-- 코드를 입력하세요
SELECT p.product_code, sum(p.price * os.sales_amount) as SALES
from product p, OFFLINE_SALE os
where p.product_id = os.product_id
group by p.product_code
order by SALES desc, product_code