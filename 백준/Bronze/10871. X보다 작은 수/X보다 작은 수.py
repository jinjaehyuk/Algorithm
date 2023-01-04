N, X = map(int,input().split())
N_list = list(map(int, input().split()))
X_list =[] 
for i in range(len(N_list)):
    if N_list[i] < X:
        X_list.append( N_list[i])

print(*X_list)