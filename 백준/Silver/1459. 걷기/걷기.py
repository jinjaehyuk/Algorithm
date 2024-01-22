import sys 
input = sys.stdin.readline
x,y,w,s=  map(int,input().split())

# 평행
t1 = (x+y) *w

# 대각선
if (x+y) %2 == 0:
    t2 = max(x,y) *s
else:
    t2 = (max(x,y)-1) * s + w

#평행 + 대각선
t3 = (min(x,y) * s) + (abs(x-y) * w)

print(min(t1,t2,t3))