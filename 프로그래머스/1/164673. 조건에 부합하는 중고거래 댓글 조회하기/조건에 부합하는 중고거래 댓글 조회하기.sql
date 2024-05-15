-- 코드를 입력하세요
select ugb.TITLE,ugb.BOARD_ID,REPLY_ID,ugr.WRITER_ID,ugr.CONTENTS,DATE_FORMAT(ugr.CREATED_DATE,"%Y-%m-%d") as CREATE_DATE
from used_goods_board ugb, used_goods_reply ugr
where ugb.board_id = ugr.board_id
and ugb.created_date like '2022-10%'
order by ugr.created_date asc, ugb.title

