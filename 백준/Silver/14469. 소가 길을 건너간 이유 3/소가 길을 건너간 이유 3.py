N = int(input())    

a=[]
for i in range(N):
    a.append(list(map(int,input().split())))
    
a = sorted(a,key=lambda x:x)


sum1 = sum(a[0])
temp = 0
for i in range(N-1):
    if sum1 > a[i+1][0]:
        sum1 = sum1 + a[i+1][1]
    else:
        sum1 = sum(a[i+1])
        
    
print(sum1)