import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)    
tp = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
    dp[i+1] = max(dp[i+1], dp[i])
    
    if i + tp[i][0] <= n:
        dp[i+tp[i][0]] = max(dp[i+tp[i][0]], dp[i] + tp[i][1] )
print(dp[n])
            
