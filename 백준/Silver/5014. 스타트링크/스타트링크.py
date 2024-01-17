import sys
from collections import deque
input = sys.stdin.readline

# F = 총 층수
# S = 지금 층수
# G = 목적지
# U = X 층 위로
# D = X 층 아래로
def bfs(v):
    queue = deque([v])
    while queue:
        x = queue.popleft()
        if x == g:
            break
        for dx in [x+u,x-d]:
            if dx == x:
                continue
            if 1<= dx < (f+1) and not visited[dx]:
                queue.append(dx)
                visited[dx] = visited[x] + 1
f,s,g,u,d = map(int,input().split())
visited = [0]*(f+1)
bfs(s)

if s == g:
    print(0)
elif not visited[g]:
    print("use the stairs")
else:
    print(visited[g])