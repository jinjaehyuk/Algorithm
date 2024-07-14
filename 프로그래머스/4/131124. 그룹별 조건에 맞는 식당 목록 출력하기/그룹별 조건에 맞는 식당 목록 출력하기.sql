-- 코드를 입력하세요

SELECT mp.member_name,rr.review_text, date_format(review_date,'%Y-%m-%d') as review_date
from MEMBER_PROFILE mp, Rest_review rr
where mp.member_id = rr.member_id 
and rr.member_id =
(select member_id 
 from Rest_Review 
 group by member_id 
 order by count(*) desc limit 1)
 order by review_date, review_text