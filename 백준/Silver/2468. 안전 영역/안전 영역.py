import sys
from collections import deque
input = sys.stdin.readline



dx = [-1,1,0,0]
dy = [0,0,-1,1]

#i = x
#j = y
#k = 빗물 높이
def bfs(i,j,k):
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    while queue:
        x,y = queue.popleft()
        # print(x,"/",y)
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < n and graph[nx][ny] > k and not visited[nx][ny]:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                
    

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

max_value = max(map(max,graph))
min_value = min(map(min,graph))
result = []
for k in range(min_value-1,max_value):
    count = 0
    visited = [[0]* n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                bfs(i,j,k)
                count +=1
    result.append(count)
print(max(result))                