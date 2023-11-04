T = int(input())

for _ in range(T):
    N = int(input())
    a = list(input().split())
    result =[a[0]]
    for i in range(1,N):
        if ord(result[0]) >= ord(a[i]):
            result.insert(0,a[i])
        else:
            result.append(a[i])
    print("".join(result))