import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque([v])
    while queue:
        x = queue.popleft()
        if x == k:
            break
        for i in [x-1,x+1,2*x]:
            if 0<= i < 100001 and not visited[i]:
                queue.append(i)
                visited[i] = visited[x] + 1
                
visited = [0] * 100001
n,k = map(int,input().split())
bfs(n)
print(visited[k])