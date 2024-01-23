import sys 
input = sys.stdin.readline
from collections import deque

# d = 1
# for _ in range(4):
#     d = 0
#     print(d," = ", (d-1)%4)
n,m = map(int,input().split())
r,c,d = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(n)]
# 반시계로 90도
#북-0 동-1 남-2 서-3
dr = [-1,0,1,0]
dc = [0,1,0,-1]

queue = deque()
queue.append((r,c,d))
graph[r][c] = 2
cnt = 1
while queue:
    flag = 0
    x,y,d = queue.popleft()
    for _ in range(4):
        d = (d +3) % 4
        nr = x + dr[d]
        nc = y + dc[d]
        if 0<= nr < n and 0<= nc < m and graph[nr][nc] == 0:
            cnt += 1
            queue.append((nr,nc,d))
            graph[nr][nc] = 2
            flag = 1
            break
    if flag == 0:
        if graph[x-dr[d]][y-dc[d]] == 1:
            print(cnt)
            break
        else:
            queue.append((x-dr[d],y-dc[d],d))