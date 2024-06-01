-- 코드를 작성해주세요
select id, case when size_of_colony <= 100 then 'LOW' else 
        case when size_of_colony between 101 and 1000 then 'MEDIUM' else 'HIGH' end 
       end as size
from ecoli_data
order by id 