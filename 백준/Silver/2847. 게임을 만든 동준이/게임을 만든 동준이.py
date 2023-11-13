N = int(input())    

a = []
for _ in range(N):
    a.append(int(input()))
cnt = 0
for i in range(N-1,0, -1):
    if not a[i] > a[i-1]:
        while True:
            cnt +=1
            a[i-1] -= 1
            if a[i] > a[i-1]:
                break
print(cnt)