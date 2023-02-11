N = list(map(int,input()))
N = sorted(N,reverse=True)
M=''
for i in range(len(N)):
    print(N[i],end='')