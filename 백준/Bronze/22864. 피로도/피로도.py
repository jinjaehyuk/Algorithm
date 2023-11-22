# A = 쌓이는 피로도양
# B = 일한 양
# C = 휴식하면 줄어드는 피로도양
# M = MAX 피로도

A, B, C, M = map(int,input().split())

tot_work = 0 #총 일한양
tot_pi  = 0 #쌓인 피로도
time = 0 # 24시간
if A> M : tot_work = 0
else:
    while time != 24:
        time += 1 
        if tot_pi + A <= M:
            tot_work += B
            tot_pi += A
        else:
            if tot_pi - C >= 0:
                tot_pi -= C
            else:
                tot_pi = 0
print(tot_work)    