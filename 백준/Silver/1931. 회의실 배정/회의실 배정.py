N = int(input())
p = [[0]*2] * N

for i in range(N):
    p[i] = list(map(int, input().split()))

p.sort(key=lambda x:(x[1], x[0]))
# p.sort(key=lambda y:y[1])

time = 0
result = 0
for i in range(N):
    if time <= p[i][0]:
        time = p[i][1]
        result += 1
    
    
print(result)