import sys
input = sys.stdin.readline 

T= int(input())
for i in range(T):
    n = int(input())
    k = []
    k.append(0)
    k.append(1)
    for i in range(2,50):
        k.append(k[i-1] + k[i-2])
        if k[i] > n:
            break
    k.sort(reverse=True)
    result = []
    for i in range(len(k)):
        if k[i] <= n and n != 0:
            n -= k[i]
            result.append(k[i])
            
        else:
            continue
    result.sort()
    for i in result: print(i, end = " ")
    print()
