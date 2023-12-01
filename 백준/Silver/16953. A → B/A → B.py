import sys
input = sys.stdin.readline

A, B = map(int,input().split()) 

cnt = 0
while True:    
    cnt += 1  
    if A == B:
        break
    tmp = B
    if B % 2 == 0:
        B = B // 2        
    elif B % 10 == 1:
        B = B // 10
    if tmp == B:
        cnt = -1
        break
print(cnt)