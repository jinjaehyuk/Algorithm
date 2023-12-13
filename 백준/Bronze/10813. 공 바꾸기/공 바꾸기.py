import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a = [i for i in range(1,n+1)]

for i in range(m):
    x,y = map(int,input().split())
    temp = a[y-1]
    a[y-1] = a[x-1]
    a[x-1] = temp

for i in a:
    print(i,end =' ')