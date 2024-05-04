-- 코드를 작성해주세요
select fi.id, fni.fish_name, fi.length
from fish_info fi, fish_name_info fni
where fi.fish_type = fni.fish_type
and (fni.fish_type, fi.length) in (
select fish_type, max(length)
    from fish_info
    group by fish_type
)
order by fi.id asc