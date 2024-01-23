import sys 
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

queue = deque()
def bfs():
    while queue:
        z,x,y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<= nx< n and 0<= ny<m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1
                queue.append((nz,nx,ny))

m,n,h = map(int,input().split())

tomato = [ [list(map(int,input().split())) for _ in range(n)] for _ in range(h)]


for z in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[z][i][j] == 1:
                queue.append((z,i,j))
bfs()
max_value = 0
flag = 0
for z in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[z][i][j] == 0:
                flag =1
                break
            if max_value < tomato[z][i][j]:
                max_value = tomato[z][i][j]
if flag == 1:
    print(-1)
else:
    print(max_value-1)