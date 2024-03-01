import sys
input = sys.stdin.readline

n,k = map(int,input().split())
dp = [10001] *(k+1)

a=[]
for _ in range(n):
    coins = int(input())
    a.append(coins)

dp[0] = 0
for coin in a:
    for i in range(coin,k+1):
        if dp[i] > 0:
            dp[i] = min(dp[i], dp[i - coin]+1)
    
print(-1 if dp[k] == 10001  else dp[k])