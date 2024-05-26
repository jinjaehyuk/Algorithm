-- 코드를 입력하세요
SELECT b.book_id, a.author_name, date_Format(b.PUBLISHED_DATE,"%Y-%m-%d")
from book b, author a
where b.author_id = a.author_id
and b.category ='경제'
order by PUBLISHED_DATE