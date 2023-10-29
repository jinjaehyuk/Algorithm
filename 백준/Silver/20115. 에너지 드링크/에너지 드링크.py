N = int(input())   


a=[]
a = list(map(int,input().split()))
a.sort(reverse=True)
sum = 0
for i in range(len(a)):
    if i == 0 :
        sum += float(a[i])
    else:
        sum += float(a[i]) / 2 

if sum.is_integer():
    print(int(sum))
else:
    print(sum)