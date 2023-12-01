import sys
input = sys.stdin.readline

T = int(input())    

for _ in range(T):
    N = int(input())
    a = []
    for _ in range(N):
        x,y = map(int,input().split())
        a.append((x,y))
    a.sort()
    cnt = 1
    x = a[0][1]
    for i in range(1,len(a)):
        if a[i][1] < x:
            x = a[i][1]
            cnt += 1
            # print(cnt)
    print(cnt)