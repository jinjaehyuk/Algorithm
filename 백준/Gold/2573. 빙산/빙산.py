import sys 
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(min(len(dx),len(dy))):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and not visited[nx][ny] and graph[nx][ny] >0:
                visited[nx][ny] = 1
                queue.append((nx,ny))
            if 0<= nx < n and 0<= ny < m and graph[nx][ny] <= 0:
                vis_cnt[x][y] += 1                    
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
year = 0
cnt = 0
while cnt < 2:
    visited = [[0] * m for _ in range(n)]
    vis_cnt = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j] :
                cnt += 1
                bfs(i,j)
            graph[i][j] -= vis_cnt[i][j]
            if graph[i][j] < 0: graph[i][j] = 0
    if cnt == 0:
        year = 0
        break
    elif cnt == 1:
        cnt = 0  
        year += 1
           
print(year)
    