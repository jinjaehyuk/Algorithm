import sys
input = sys.stdin.readline

# N = 문제수
# L = 문제를 풀 수 있는 역량
# K = 풀수 있는 문제 최대개수
N, L, K = map(int,input().split())

mon = []
for i in range(N):
    mon.append(list(map(int,input().split())))
    
mon1 = sorted(mon, key =lambda x:x[1])
result = 0
cnt = 0
for i in range(N):
    if cnt == K:
        break
    if mon1[i][1] <= L and cnt <= K:
        result += 140
        cnt += 1
    elif mon1[i][0] <= L and cnt <= K:
        result += 100
        cnt += 1
print(result)