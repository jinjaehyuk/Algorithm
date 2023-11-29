import sys
input = sys.stdin.readline

N, M = map(int,input().split())

dna = []
for _ in range(N):
    dna.append(list(input().rstrip()))
    
i = 0
total_cnt = 0
total_list = []
for j in range(M):
    a_cnt = 0
    t_cnt = 0
    g_cnt = 0
    c_cnt = 0
    for i in range(N):
        if dna[i][j] == 'A':
            a_cnt += 1
        elif dna[i][j] == 'T':
            t_cnt += 1
        elif dna[i][j] == 'G':
            g_cnt += 1
        else:
            c_cnt += 1
    if max(a_cnt,t_cnt,g_cnt,c_cnt) == a_cnt:
        total_list.append('A')            
        total_cnt += t_cnt + g_cnt + c_cnt
    elif max(a_cnt,t_cnt,g_cnt,c_cnt) == c_cnt:
        total_list.append('C')            
        total_cnt += a_cnt + t_cnt + g_cnt
    elif max(a_cnt,t_cnt,g_cnt,c_cnt) == g_cnt:
        total_list.append('G')            
        total_cnt += a_cnt + t_cnt + c_cnt
    else:
        total_list.append('T')            
        total_cnt += a_cnt + g_cnt + c_cnt

print(''.join(total_list))
print(total_cnt)