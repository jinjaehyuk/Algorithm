N, M =map(int,input().split())  
a = list(map(int,input().split()))
a.sort()
b = sorted(a,reverse=True)

sum = 0
for i in range(N//2):
    if a[i] + b[i] >= M:
        sum += 1
print(sum)