SELECT ai.animal_id, ai.animal_type, ai.name
from animal_ins ai left outer join  animal_outs ao on ai.animal_id = ao.animal_id
where ai.sex_upon_intake like 'Intact%' and 
 ao.SEX_UPON_OUTCOME not like 'Intact%'