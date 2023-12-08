import sys
input = sys.stdin.readline

B, C, D = map(int,input().split())

#버거 가격
b_price = list(map(int, input().split()))
#사이드 가격
c_price = list(map(int, input().split()))
#음료가격
d_price = list(map(int, input().split()))

b = sorted(b_price,reverse=True)
c = sorted(c_price,reverse=True)
d = sorted(d_price,reverse=True)
min_value = min(B,C,D)

result = 0
for i in range(min_value):
    result += int((b[i]+c[i]+d[i])*0.9)

result += sum(b[min_value::])
result += sum(c[min_value::])
result += sum(d[min_value::])
    

print(sum(b_price)+sum(c_price)+sum(d_price))
print(result)
