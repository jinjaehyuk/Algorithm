-- 코드를 입력하세요
SELECT b.author_id, author_name, category, sum(sales * price) as total_sales
from author a, book b, book_sales bs
where a.author_id = b.author_id
and b.book_id = bs.book_id
and bs.sales_date like '2022-01%'
group by b.author_id, author_name, category
order by author_id, category desc 