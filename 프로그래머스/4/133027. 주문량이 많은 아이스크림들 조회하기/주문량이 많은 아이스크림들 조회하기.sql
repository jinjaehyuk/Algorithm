-- 코드를 입력하세요
SELECT  a.flavor
from first_half a, july b
where a.flavor = b.flavor
group by a.flavor
HAVING SUM(A.TOTAL_ORDER + B.TOTAL_ORDER)
order by SUM(A.TOTAL_ORDER + B.TOTAL_ORDER) desc
limit 3