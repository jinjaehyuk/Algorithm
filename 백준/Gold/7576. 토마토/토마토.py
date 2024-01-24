import sys 
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]  
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

m,n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))
            
bfs()

flag = False
for i in range(n):
    if 0 in graph[i]:
        flag = True
        break
if flag:
    print(-1)
else:
    print(max(map(max,graph)) -1)