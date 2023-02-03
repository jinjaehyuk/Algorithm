C = int(input())

for _ in range(C):
    N = list(map(int,input().split()))
    N = N[0:N[0]+1]
    avg = sum(N[1:]) / N[0]
    cnt = 0
    for i in range(1,len(N),1):
        if avg < N[i]:
            cnt += 1
    stu_avg = round(cnt/N[0] *100,3)
    print('%.3f' % stu_avg,'%', sep='')