N = []
max_num = 0
m,n=0,0
for i in range(9):
    N = list(map(int,input().split()))
    if max_num < max(N):
        max_num = max(N)
        m,n = i, N.index(max_num)

print(max_num)
print(m+1,n+1, sep =' ')