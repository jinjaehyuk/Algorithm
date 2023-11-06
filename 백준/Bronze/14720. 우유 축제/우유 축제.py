N = int(input())

a = list(map(int,input().split()))
b = a.index(0)
    
count =1
temp = a[b]
for i in range(b,N):
    if temp+1 == a[i]:
        count += 1
        temp = a[i]
    elif temp == a[i] + 2 :
        count +=1
        temp = a[i]
print(count)