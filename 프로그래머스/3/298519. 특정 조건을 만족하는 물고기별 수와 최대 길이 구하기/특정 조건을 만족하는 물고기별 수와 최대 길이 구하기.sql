-- 코드를 작성해주세요
select count(id) fish_count, max(length) as max_length, fish_type
from (
    select id,fish_type, 
            case when length is null then ifnull(length,10) else 
                case when length <= 10 then 10 else length end
            end as length, time
    from fish_info
    ) b
group by fish_type
having avg(length) > 33
order by fish_type
