-- 코드를 입력하세요
select concat('/home/grep/src/',ugb.board_id,'/',file_id,file_name,file_ext) as file_path
from USED_GOODS_FILE ugf,USED_GOODS_BOARD ugb
where ugf.board_id = ugb.board_id
and views = (select max(views) from USED_GOODS_BOARD)
order by file_id desc