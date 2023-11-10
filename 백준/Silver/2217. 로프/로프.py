N = int(input())

a = [int(input()) for _ in range(N)]
a.sort(reverse=True)

b = []
for i in range(N):
    b.append(int(a[i])*(i+1))
    
print(max(b))