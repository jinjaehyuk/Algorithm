N = int(input())
A = []
B = []
A = list(map(int,input().split()))
B = list(map(int,input().split())) 

A.sort()
sum = 0
for i in range(N):
    sum += A[i] * max(B)
    B.remove(max(B))
print(sum)
    