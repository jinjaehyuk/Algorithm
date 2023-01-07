N = int(input())

for i in range(N):
    for j in range(N,0,-1):
        if(j>i+1):
           print(' ',end='')
        else:
            print('*',end='')
    print()