n = int(input())
p = list(map(int,input().split()))

p.sort()

result= 0
for i in range(n):
    for j in range(0,i+1):
        result += int(p[j])
print(result)