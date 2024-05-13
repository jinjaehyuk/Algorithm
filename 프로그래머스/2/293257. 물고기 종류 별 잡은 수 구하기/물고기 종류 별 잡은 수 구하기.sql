-- 코드를 작성해주세요

select count(*) as fish_count, fni.fish_name
from fish_info fi, fish_name_info fni
where fi.fish_type = fni.fish_type
group by fi.fish_type, fni.fish_name
order by fish_count desc