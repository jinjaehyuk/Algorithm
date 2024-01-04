import sys
input = sys.stdin.readline
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m = map(int,input().split())


def bfs(i,j,div):
    queue = deque()
    queue.append((i,j))
    count = 1
    war[i][j] = 'X'
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0<= nx < m and 0<= ny < n and war[nx][ny] == div:
                war[nx][ny] ='X'
                count += 1
                queue.append((nx,ny))
                  
    return count ** 2



war = []
for _ in range(m):
    war.append(list(input().rstrip()))


w_temp = []
b_temp = []
for i in range(m):
    for j in range(n):
        if war[i][j] == 'W':
            w_temp.append(bfs(i,j,'W'))
        elif war[i][j] == 'B':
            b_temp.append(bfs(i,j,'B'))
           
print(sum(w_temp), sum(b_temp))
    