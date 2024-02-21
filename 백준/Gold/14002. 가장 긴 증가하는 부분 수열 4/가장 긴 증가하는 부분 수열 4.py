import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
dp = [1] * n


for i in range(n):
    for j in range(i, n):
        if a[i] < a[j]:
            dp[j] = max(dp[j], dp[i]+1)
      
max_dp = max(dp)            
print(max_dp)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == max_dp:
        result.append(a[i]) 
        max_dp -= 1
result.reverse()

for i in result:
    print(i, end = " ")
    