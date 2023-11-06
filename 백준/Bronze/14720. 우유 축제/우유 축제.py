N = int(input())

a = list(map(int,input().split()))
count = 0

for i in range(N):
    if a[i] == count%3:
        count += 1
print(count)