N = int(input())
M = list(map(int,input().split()))
M = M[0:N]
M_max = max(M)
sum =0 
for i in range(N):
    sum += M[i]/M_max*100

print(sum/N)