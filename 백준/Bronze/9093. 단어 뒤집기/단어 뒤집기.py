import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    
    a = list(input().split())    
    
    for i in range(len(a)):
        str = []
        for j in range(len(a[i])-1,-1,-1):
            str.append(a[i][j])
        a[i] = ''.join(str)
    print(' '.join(a))    
    