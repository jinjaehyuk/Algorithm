import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
    s = 0
    w = 0
    queue = deque()
    queue.append((a,b))
    
    if graph[a][b] == 'o':
        s += 1
    elif graph[a][b] =='v':
        w += 1
    
    graph[a][b] ='#'
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#':
                if graph[nx][ny] == 'o':
                    s += 1
                elif graph[nx][ny] =='v':
                    w += 1
                graph[nx][ny]='#'
                queue.append((nx,ny))
    if w >= s:
        return 0, w
    elif s > w:
        return s, 0
    
r,c = map(int,input().split())
graph = []

total_sheep = 0
total_wolf = 0
for i in range(r):
    graph.append(list(input()))

for i in range(r):
    for j in range(c):
        if graph[i][j] in 'ov':
            tempSheep, tempWolf = bfs(i, j)
            total_sheep += tempSheep
            total_wolf += tempWolf
print(total_sheep, total_wolf)