import sys
input = sys.stdin.readline
from collections import deque


# 위, 아래, 왼, 오, 대각(위 왼),위 오, 아 왼, 아 오
dx = [0,0,-1,1,1,-1,1,-1,1]
dy = [1,-1,0,0,1,1,1,-1,-1]

queue = deque()
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < m and not graph[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    


n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))
bfs()
print(max(map(max,graph))-1)