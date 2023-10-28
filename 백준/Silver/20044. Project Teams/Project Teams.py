n = int(input())
a = list(map(int,input().split()))

a.sort()

b = []
for i in range(n):
    b.append(a[i] + a[len(a)-1])
    a.remove(a[len(a)-1])
print(min(b))