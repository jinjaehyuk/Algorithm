-- 코드를 작성해주세요
select year(YM) as year, round(sum(PM_VAL1) / count(*), 2) as PM10,
round(sum(PM_VAL2) / count(*), 2) as 'PM2.5'
from air_pollution
where location2 ='수원'
group by year
order by year