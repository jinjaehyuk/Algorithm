import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
dp = [0]
sum = 0
for i in a:
    sum += i
    dp.append(sum)
    
for _ in range(m):
    i,j = map(int,input().split())  
    print(dp[j] - dp[i-1])
