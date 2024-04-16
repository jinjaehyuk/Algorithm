-- 코드를 입력하세요
SELECT FLOOR(sum(daily_Fee)/ count(*)) as AVERAGE_FEE
FROM CAR_RENTAL_COMPANY_CAR
WHERE car_type ='SUV'