-- 코드를 입력하세요
-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성해주세요.
SELECT a.APNT_NO,	p.PT_NAME,	a.PT_NO,	d.MCDP_CD,	d.DR_NAME,	a.APNT_YMD
from patient p, doctor d, appointment a
where p.pt_no = a.pt_no and d.dr_id = a.mddr_id 
and to_char(APNT_YMD,'YYYYMMDD') = '20220413'
and a.mcdp_cd = 'CS'
and a.APNT_CNCL_YN ='N' and a.APNT_CNCL_YN is not null
order by apnt_ymd 