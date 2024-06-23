-- 코드를 입력하세요
select category, price as max_price, product_name
from FOOD_PRODUCT
where (category, price) in
(select category, max(price) as  price
from food_product
 where category in ('과자','국','김치','식용유')
 group by category
)
order by price desc 