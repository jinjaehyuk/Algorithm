N = int(input())    

a = list(map(int,input().split()))
b = list(map(int,input().split()))


sum = 0
for i in range(N):
    result = a[i] - b[i]
    if result > 0:
        sum += result
print(sum)