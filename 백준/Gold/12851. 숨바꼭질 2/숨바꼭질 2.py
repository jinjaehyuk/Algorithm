import sys
input = sys.stdin.readline
from collections import deque


def bfs(i):
    global result
    queue = deque([i])
    visited[i] = 0
    while queue:
        x = queue.popleft()
        if x == k:
            result += 1
            continue
        for nx in (x*2, x+1,x-1):
            if 0 <= nx < 100001 and (visited[nx] == -1 or visited[nx] == visited[x] + 1):
                visited[nx] = visited[x] + 1
                queue.append(nx)
    

n,k = map(int,input().split())

visited = [-1] * 100001
result = 0
bfs(n)
print(visited[k])
print(result)
