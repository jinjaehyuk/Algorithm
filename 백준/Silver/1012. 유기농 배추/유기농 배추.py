import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    a[x][y] = 0
    size = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                queue.append((nx,ny))
                a[nx][ny] = 0
                size += 1
    return size
    
T = int(input())

for _ in range(T):
    m,n,k = map(int,input().split())
    a = [[0]*m for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        a[y][x] = 1
        
    result = []
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                result.append(bfs(i,j))
               
    print(len(result))