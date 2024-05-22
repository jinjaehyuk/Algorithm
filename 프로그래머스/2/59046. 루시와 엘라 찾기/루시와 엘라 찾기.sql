-- 코드를 입력하세요
SELECT ANIMAL_ID, name, sex_upon_intake
from ANIMAL_INS
where sex_upon_intake = 'Spayed Female'
and name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
order by ANIMAL_ID