import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int,input().split()))
dp = [1] * (n)

for i in range(n): 
    for j in range(i,n): 
        if a[i] < a[j]:
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))