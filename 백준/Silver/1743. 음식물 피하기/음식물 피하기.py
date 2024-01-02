import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    size = 1
    graph[a][b] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 1<= nx <= n and 1 <= ny <= m and graph[nx][ny] == 1:
                size += 1
                queue.append((nx,ny))
                graph[nx][ny] = 0
    return size


n,m,k = map(int,input().split())

graph = [[0]*(m+1) for _ in range((n+1))]

for _ in range(k):
    r,c = map(int,input().split())
    graph[r][c]=1

result = []
for i in range(1,n+1):
    for j in range(1,m+1):
        if graph[i][j] == 1:
            result.append(bfs(i,j))
print(max(result))