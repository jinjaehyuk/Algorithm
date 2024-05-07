-- 코드를 입력하세요
SELECT fp.product_id, fp.product_name, sum(fp.price * fo.amount) as TOTAL_SALES
from food_product fp, food_order fo
where fp.product_id = fo.product_id
and produce_date like '2022-05%'
group by product_id
order by total_sales desc, fp.product_id asc