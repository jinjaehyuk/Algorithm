
a = [300, 60, 10]

C = int(input())
for i in range(len(a)):
    if C %10 == 0 :
        print(C//a[i], end =' ')
        C %= a[i]
    else:
        print(-1)
        break