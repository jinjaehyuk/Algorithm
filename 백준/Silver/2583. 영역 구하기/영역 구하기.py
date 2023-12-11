###DFS
# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# M, N, K = map(int,input().split())

# graph = [[0]*N for _ in range(M)]

# for _ in range(K):
#     x1, y1, x2, y2 = map(int,input().split())
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             graph[i][j] = 1
# #상하좌우
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# count = 0
# def dfs (x, y):
#     global count
#     graph[x][y] = 1
#     count +=1
#     for i in range(4):
       
#         nx = x + dx[i] 
#         ny = y + dy[i]
#         if 0<= nx < M and 0<= ny < N and graph[nx][ny]==0:

#             dfs(nx,ny)

#     return count

# result = []
# for i in range(M):
#     for j in range(N):
#         if graph[i][j] == 0:
#             result.append(dfs(i,j))
#             count = 0
# print(len(result))
# result.sort()
# for i in result:
#     print(i,end=' ')           



###BFS
from collections import deque
import sys
input = sys.stdin.readline

M, N, K = map(int,input().split())

graph = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
#상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 1
    size = 1
    while queue:
        x, y= queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] 
            if 0<= nx < M and 0<= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx,ny))
                size += 1
    result.append(size)
        
result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            bfs(i,j)
print(len(result))
result.sort()
for i in result:
    print(i,end=' ')   