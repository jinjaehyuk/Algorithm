N,K = map(int,input().split())
N_list = []

try:
    for i in range(1,N+1):
            if N % i ==0:
                N_list.append(i)

    print(N_list[K-1])
except:
    print(0)            