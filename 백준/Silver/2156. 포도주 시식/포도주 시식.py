import sys
input = sys.stdin.readline
n = int(input())    
a = [0] * (n+1)
dp = [0] * (n+1)
for i in range(1,n+1):
    a[i] = int(input())
if n > 0:
    dp[1] = a[1]
if n > 1: 
    dp[2] = a[2] + a[1]
if n > 2:
    dp[3] = max(a[2]+a[3], a[3]+a[1],dp[2])
    for i in range(4,n+1):
        dp[i] = max(a[i] + dp[i-2], a[i]+a[i-1]+dp[i-3], dp[i-1])
print(dp[n])
