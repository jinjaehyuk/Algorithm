N, K =map(int,input().split()) 


a = list(map(int,input().split()))
b= [] 
for i in range(1 ,N):
    b.append(a[i] - a[i-1])
sum = 0
b.sort()
for i in range(N-K):
    sum += b[i]
    
print(sum)