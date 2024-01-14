import sys

from collections import deque
input = sys.stdin.readline


def bfs(v):
    queue = deque([v])
    visited[v] = 1
    while queue:
        x = queue.popleft()
        for i in rel[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[x] + 1
            
            

n = int(input())
a,b = map(int,input().split())

m = int(input())

rel = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    x, y = map(int,input().split())
    rel[x].append(y)
    rel[y].append(x)

bfs(min(a,b))
print(visited[max(a,b)]-visited[min(a,b)])