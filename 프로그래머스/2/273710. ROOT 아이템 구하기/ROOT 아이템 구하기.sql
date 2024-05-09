-- 코드를 작성해주세요
select item_id, item_name
From  item_info
where item_id in ( select item_id from item_tree where PARENT_ITEM_ID is null )
order by item_id