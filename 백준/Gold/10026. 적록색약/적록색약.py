###BFS

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

a = [list(input().rstrip()) for _ in range(N)]
a_chk = [[0]*N for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    a_chk[x][y] = 1
    color = a[x][y]
    size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and 0<= ny<N and a_chk[nx][ny]==0:
                if color == a[nx][ny]:
                    a_chk[nx][ny] = 1
                    queue.append((nx,ny))
                    size += 1
    result.append(size)          
result = []
for i in range(N):
    for j in range(N):
        if a_chk[i][j] == 0:
            bfs(i,j)
result1 = result 
         
a_chk = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if a[i][j] == 'G':
            a[i][j] = 'R'
result = []
for i in range(N):
    for j in range(N):
        if a_chk[i][j] == 0:
            bfs(i,j)
        
print(len(result1),len(result))
