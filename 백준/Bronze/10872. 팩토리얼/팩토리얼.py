N = int(input())
if N == 0:
    print('1')
else:
    sum = 1
    for i in range(N):
        sum *= (i+1)
    print(sum)