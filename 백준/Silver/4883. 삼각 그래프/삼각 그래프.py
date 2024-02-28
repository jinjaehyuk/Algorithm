import sys
input = sys.stdin.readline

cnt = 0

while True:   
    n = int(input())   
    if n == 0:
        break
    cnt += 1
    a = []
    for _ in range(n):
        a.append(list(map(int,input().split())))
    dp = [[0]*3 for _ in range(n)]
    dp[0] = a[0]
    start = dp[0][1]
    dp[0][2] += start
    dp[1][0] = start + a[1][0]
    dp[1][1] += min(start+a[1][1], dp[1][0]+a[1][1], dp[0][2]+a[1][1])
    dp[1][2] += min(start+a[1][2], dp[1][1]+a[1][2], dp[0][2]+a[1][2])
    for i in range(2,n):
        for j in range(3):
            if j == 0:
                dp[i][j] = min(dp[i-1][j] + a[i][j], dp[i-1][j+1] + a[i][j])
            elif j == 1: # 2,1
                dp[i][j] = min(dp[i-1][j-1] + a[i][j], dp[i-1][j] + a[i][j], dp[i][j-1]+a[i][j],dp[i-1][j+1]+a[i][j])
            else: # 2,2
                dp[i][j] = min(dp[i-1][j-1] + a[i][j], dp[i-1][j] + a[i][j], dp[i][j-1]+a[i][j],dp[i-1][j-1]+a[i-1][j]+a[i][j])
    print("{0}. {1}".format(cnt,dp[n-1][1]))