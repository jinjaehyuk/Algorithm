## 영식 요금제 (Y) 30초마다 10원씩
## 0~29  = 10원 | 30 ~ 59 = 20원
def y_money(time):
    time_cash = 10
    limit_time = 30
    total_money = ((time//limit_time)+1)*time_cash
    return int(total_money)
## 민식 요금제 (M) 60초마다 15원
## 0 ~ 59 = 15원 | 60 ~ 119 = 30원
def m_money(time):
    time_cash = 15
    limit_time = 60
    total_money = ((time//limit_time)+1)*time_cash
    return int(total_money)

## 통화의 개수 N
N = int(input())
## N개를 입력
call = list[N]
call = input().split()

y_total =0
m_total =0

for i in range(N):
    y_total += y_money(int(call[i]))
    m_total += m_money(int(call[i]))

if( y_total < m_total ):
    print("Y",y_total)
elif (y_total > m_total):
    print("M",m_total)
elif (y_total == m_total):
    print("Y","M",y_total)
    

