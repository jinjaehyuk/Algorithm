N = int(input())    

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort()
sum = 0 
for i in range(N):
    sum += abs(a[i])
    sum += abs(b[i])
    
print(sum)