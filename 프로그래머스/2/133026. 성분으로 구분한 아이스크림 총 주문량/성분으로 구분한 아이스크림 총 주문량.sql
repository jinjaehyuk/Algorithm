-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order
from first_half fh, icecream_info ii
where fh.flavor = ii.flavor
group by ingredient_type 