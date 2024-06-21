-- 코드를 입력하세요
select user_id, nickname,total_sales
from USED_GOODS_USER ugu,
(
SELECT WRITER_ID, sum(price) as total_sales
from USED_GOODS_BOARD
where status ='DONE'
group by WRITER_ID
having sum(price)>=700000
) b
where ugu.user_id = b.writer_id
order by total_sales