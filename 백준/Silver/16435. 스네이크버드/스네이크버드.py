N, L = input().split()
N = int(N)
L = int(L)

h = list(map(int,input().split()))

h.sort()

for i in range(N):
    if L >= h[i]:
        L += 1
print(L)