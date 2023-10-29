N = int(input())   

a = []

for i in range(N):
    a.append(int(input()))

a.sort(reverse=True)
temp = 0
for i in range(N):
    if (i+1)%3 == 0:
        temp += a[i]
print(sum(a)- temp)