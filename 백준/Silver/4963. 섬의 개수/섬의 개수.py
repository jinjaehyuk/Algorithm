# import sys
# from collections import deque
# input = sys.stdin.readline


# dx = [-1,1,0,0,-1,-1,1,1]
# dy = [0,0,-1,1,-1,1,-1,1]
# result = []
# while True:
    
#     w,h = map(int,input().split())
    
#     if w == 0 and h == 0:
#         break
    
#     graph=[]
#     for i in range(h):
#         graph.append(list(map(int,input().split())))
    
#     def bfs(x,y):
#         queue = deque()
#         queue.append((x,y))
#         graph[x][y] = 0
#         count = 1
#         while queue:
#             x, y = queue.popleft()
#             for i in range(8):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < h and 0<= ny < w and graph[nx][ny] == 1:
#                     graph[nx][ny] = 0
#                     queue.append((nx, ny))
#                     count += 1
#         return count  
#     cnt = []
#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1:
#                 cnt.append(bfs(i,j))
#     result.append(len(cnt))
# for i in result:
#     print(i)
import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]
result = []
while True:
    w,h = map(int,input().split())
    
    if w == 0 and h == 0:
        break
    
    graph=[]
    for i in range(h):
        graph.append(list(map(int,input().split())))
    count = 0
    def dfs(x,y):
        global count
        graph[x][y] = 0
        count += 1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0<= ny < w and graph[nx][ny] == 1:
                dfs(nx,ny)
        return count      
    
    cnt = []
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt.append(dfs(i,j))
                count = 0
    result.append(len(cnt))
for i in result:
    print(i) 