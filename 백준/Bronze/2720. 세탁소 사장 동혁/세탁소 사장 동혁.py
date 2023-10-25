T = int(input())
a = [25,10,5,1]


for i in range(T):
    C = int(input())
    for i in range(len(a)):
        print(C//a[i], end = ' ')
        C %= a[i]