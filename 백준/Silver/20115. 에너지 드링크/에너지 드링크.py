N = int(input())   


a=[]
a = list(map(int,input().split()))
a.sort(reverse=True)
sum = 0
for i in range(len(a)):
    if i == 0 :
        sum += a[i]
    else:
        sum += a[i] / 2 

print(sum)