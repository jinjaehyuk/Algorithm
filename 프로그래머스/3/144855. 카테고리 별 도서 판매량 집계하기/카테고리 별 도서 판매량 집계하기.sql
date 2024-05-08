-- 코드를 입력하세요
SELECT category, sum(bs.sales) as TOTAL_SALES
from book b, book_sales bs
where b.book_id = bs.book_id
and bs.sales_date like '2022-01%'
group by category
order by category 