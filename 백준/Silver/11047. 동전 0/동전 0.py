n, k = input().split()
n = int(n)
k = int(k)
a = []
for i in range(n):
    a.append(int(input()))
    
result = 0
for i in range(n-1, -1, -1):
    result += int(k/a[i])
    k %= a[i]

print(result)