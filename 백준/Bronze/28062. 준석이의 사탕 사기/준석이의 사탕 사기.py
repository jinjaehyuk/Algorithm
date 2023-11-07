N = int(input())    
a = list(map(int,input().split()))

a.sort(reverse=True)
sum = sum(a)
b = []
if sum % 2 != 0:
    for i in range(len(a)):
        if a[i]%2 != 0:
            b.append(a[i])
    b.sort()
    sum -= b[0]

print(sum) 